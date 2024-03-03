"""
MIT License

Copyright (c) 2024 John Riggles

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Circuitpython module for interfacing with Azoteq trackpad modules

Datasheet: https://www.azoteq.com/images/stories/pdf/iqs5xx-b000_trackpad_datasheet.pdf
"""
import board
import busio
from adafruit_bus_device.i2c_device import I2CDevice
from countio import Counter, Edge
from micropython import const
from time import monotonic, sleep

__version__ = '0.0.0+auto.0'
__repo__ = 'https://github.com/JRiggles/IQS5XX'

# TODO: refactor to make use of adafruit-circuitpython-register
# https://github.com/adafruit/Adafruit_CircuitPython_Register

# NOTE: IQS5XX supports 'Fast I2C' at 400kHz, but a lot of CircuitPython
# hardware doesn't, and 100kHz is the default for most boards
I2C_FREQ = const(400_000)
DEVICE_ADDR = const(0x74)

PRODUCT_NOS: dict[int, str] = {
    40: 'IQS550',
    52: 'IQS525',
    58: 'IQS572',
}
# hex addresses and byte lengths for I2C registers
REGISTERS: dict[str, tuple[int, int]] = {
    # device/product info
    'device_id': (const(0xF000), const(12)),
    'product_no': (const(0x0000), const(2)),
    'project_no': (const(0x0002), const(2)),
    'major_version': (const(0x0004), const(1)),
    'minor_version': (const(0x0005), const(1)),
    'bootloader_status': (const(0x0006), const(1)),
    # touch event info
    'max_touch_info': (const(0x000B), const(8)),
    'previous_cycle_time': (const(0x000C), const(1)),
    'gesture_events_0': (const(0x000D), const(1)),
    'gesture_events_1': (const(0x000E), const(1)),
    # system configuration
    'system_info_0': (const(0x000F), const(1)),
    'system_info_1': (const(0x0010), const(1)),
    # positional/finger info
    'n_fingers': (const(0x0011), const(1)),
    'relative_x': (const(0x0012), const(2)),
    'relative_y': (const(0x0014), const(2)),
    'absolute_x': (const(0x0016), const(2)),
    'absolute_y': (const(0x0018), const(2)),
    'touch_strength': (const(0x001A), const(2)),
    'touch_areasize': (const(0x001C), const(1)),
    # finger 1 (same as un-numbered absolute & touch registers above)
    'absolute_x_1': (const(0x0016), const(2)),
    'absolute_y_1': (const(0x0018), const(2)),
    'touch_strength_1': (const(0x001A), const(2)),
    'touch_areasize_1': (const(0x001C), const(1)),
    # finger 2
    'absolute_x_2': (const(0x001D), const(2)),
    'absolute_y_2': (const(0x001F), const(2)),
    'touch_strength_2': (const(0x0021), const(2)),
    'touch_areasize_2': (const(0x0023), const(1)),
    # finger 3
    'absolute_x_3': (const(0x0024), const(2)),
    'absolute_y_3': (const(0x0026), const(2)),
    'touch_strength_3': (const(0x0028), const(2)),
    'touch_areasize_3': (const(0x002A), const(1)),
    # finger 4
    'absolute_x_4': (const(0x002B), const(2)),
    'absolute_y_4': (const(0x002D), const(2)),
    'touch_strength_4': (const(0x002F), const(2)),
    'touch_areasize_4': (const(0x0031), const(1)),
    # finger 5
    'absolute_x_5': (const(0x0032), const(2)),
    'absolute_y_5': (const(0x0034), const(2)),
    'touch_strength_5': (const(0x0036), const(2)),
    'touch_areasize_5': (const(0x0038), const(1)),
    # statuses
    'prox_status': (const(0x0039), const(32)),
    'touch_status': (const(0x0059), const(30)),
    'snap_status': (const(0x0077), const(30)),
    # raw data
    'count_values': (const(0x0095), const(300)),
    'delta_values': (const(0x01C1), const(300)),
    # advanced features
    'alp_count_value': (const(0x02ED), const(2)),
    'alp_individual_count_values': (const(0x02EF), const(20)),

    # ---- advanced features - writable registers ---
    'reference_values': (const(0x0303), const(300)),
    'alp_lta': (const(0x42F), const(2)),
    'system_control_0': (const(0x0431), const(1)),
    'system_control_1': (const(0x0432), const(1)),
    'alp_ati_compensation': (const(0x435), const(10)),
    'ati_compensation': (const(0x043F), const(150)),
    'ati_c_individual_adjust': (const(0x4D5), const(150)),
    'global_ati_c': (const(0x056B), const(1)),
    'alp_ati_c': (const(0x056C), const(1)),
    'ati_target': (const(0x056D), const(2)),
    'alp_ati_target': (const(0x056F), const(2)),
    'reference_drift_limit': (const(0x0571), const(1)),
    'alp_lta_drift_limit': (const(0x0572), const(1)),
    're_ati_lower_comp_limit': (const(0x0573), const(1)),
    're_ati_upper_comp_limit': (const(0x0574), const(1)),
    'max_count_limit': (const(0x0575), const(2)),
    're_ati_retry_time': (const(0x0577), const(1)),
    'report_rate_active_mode': (const(0x057A), const(2)),
    'report_rate_idle_touch_mode': (const(0x057C), const(2)),
    'report_rate_idle_mode': (const(0x057E), const(2)),
    'report_rate_lp1_mode': (const(0x0580), const(2)),
    'report_rate_lp2_mode': (const(0x0582), const(2)),
    'timeout_active_mode': (const(0x0584), const(1)),
    'timeout_idle_touch_mode': (const(0x0585), const(1)),
    'timeout_idle_mode': (const(0x0586), const(1)),
    'timeout_lp1_mode': (const(0x0587), const(1)),
    'reference_update_time': (const(0x0588), const(1)),
    'snap_timeout': (const(0x0589), const(1)),
    'i2c_timeout': (const(0x058A), const(1)),
    'system_config_0': (const(0x058E), const(1)),
    'system_config_1': (const(0x058F), const(1)),
    'snap_threshold': (const(0x0592), const(2)),
    'prox_threshold_trackpad': (const(0x0594), const(1)),
    'prox_threshold_alp_channel': (const(0x0595), const(1)),
    'global_touch_multiplier_set': (const(0x0596), const(1)),
    'global_touch_multiplier_clear': (const(0x0597), const(1)),
    'individual_touch_multiplier_adjustments': (const(0x0598), const(150)),
    'min_count_re_ati_delta': (const(0x062E), const(1)),
    'filter_settings_0': (const(0x0632), const(1)),
    'xy_static_beta': (const(0x0633), const(1)),
    'alp_count_beta': (const(0x0634), const(1)),
    'alp1_lta_beta': (const(0x0635), const(1)),
    'alp2_lta_beta': (const(0x0636), const(1)),
    'xy_dynamic_filter_bottom_beta': (const(0x0637), const(1)),
    'xy_dynamic_filter_lower_speed': (const(0x0638), const(1)),
    'xy_dynamic_filter_upper_speed': (const(0x0639), const(2)),
    'total_rx': (const(0x063D), const(1)),
    'total_tx': (const(0x063E), const(1)),
    'rx_mapping': (const(0x063F), const(10)),
    'tx_mapping': (const(0x0649), const(15)),
    'alp_channel_setup_0': (const(0x0658), const(1)),
    'alp_rx_select': (const(0x0659), const(2)),
    'alp_tx_select': (const(0x065B), const(2)),
    'rx_to_tx': (const(0x065D), const(1)),
    'hardware_settings_a': (const(0x065F), const(1)),
    'hardware_settings_b1': (const(0x0660), const(1)),
    'hardware_settings_b2_alp': (const(0x0661), const(1)),
    'hardware_settings_c1': (const(0x0662), const(1)),
    'hardware_settings_c2_alp': (const(0x0663), const(1)),
    'hardware_settings_d1': (const(0x0664), const(1)),
    'hardware_settings_d2_alp': (const(0x0665), const(1)),
    'xy_config_0': (const(0x0669), const(1)),
    'max_multi_touches': (const(0x066A), const(1)),
    'finger_split_aggression_factor': (const(0x066B), const(1)),
    'palm_reject_threshold': (const(0x066C), const(1)),
    'palm_reject_timeout': (const(0x066D), const(1)),
    'x_resolution_px': (const(0x066E), const(2)),
    'y_resolution_px': (const(0x0670), const(2)),
    'stationary_touch_movement_threshold_px': (const(0x0672), const(1)),
    'default_read_address': (const(0x0675), const(2)),
    'export_file_version_number': (const(0x0677), const(2)),
    'prox_debounce': (const(0x0679), const(1)),
    'touch_snap_debounce': (const(0x067A), const(1)),
    'active_channels': (const(0x067B), const(30)),
    'snap_enabled_channels': (const(0x0699), const(30)),
    'single_finger_gestures': (const(0x06B7), const(1)),
    'multi_finger_gestures': (const(0x06B8), const(1)),
    'tap_time_ms': (const(0x06B9), const(2)),
    'tap_distance_px': (const(0x06BB), const(2)),
    'hold_time_ms': (const(0x06BD), const(2)),
    'swipe_initial_time_ms': (const(0x06BF), const(2)),
    'swipe_initial_distance_px': (const(0x06C1), const(2)),
    'swipe_consecutive_time_ms': (const(0x06C3), const(2)),
    'swipe_consecutive_distance_px': (const(0x06C5), const(2)),
    'swipe_angle': (const(0x06C7), const(1)),
    'scroll_initial_distance_px': (const(0x06C8), const(2)),
    'scroll_angle': (const(0x06CA), const(1)),
    'zoom_initial_distance_px': (const(0x06CB), const(2)),
    'zoom_consecutive_distance_px': (const(0x06CD), const(2)),
}

GESTURE_EVENTS: dict[int, str] = {
    0x001: 'SINGLE_TAP',
    0x002: 'PRESS_AND_HOLD',
    0x004: 'SWIPE_RIGHT',
    0x008: 'SWIPE_LEFT',
    0x010: 'SWIPE_UP',
    0x020: 'SWIPE_DOWN',
    0x040: 'TWO_FINGER_TAP',
    0x080: 'SCROLL',
    0x100: 'ZOOM',
}


class IQS5XX:
    """
    Azoteq IQS5XX Trackpad Module Interface

    :param ready_pin: The pin to which the device's ready pin is connected
    :type ready_pin: ~board.PIN
    :param scl: The SCL pin for I2C communication (default is `board.SCL1`)
    :type scl: ~board.PIN, optional
    :param sda: The SDA pin for I2C communication (default is `board.SDA1`)
    :type sda: ~board.PIN, optional
    """
    # use __slots__ to add register names as class attributes
    # NOTE: splat syntax (*REGISTERS) is not supported, so list() is used here
    __slots__ = ('__dict__', list(REGISTERS.keys()))

    def __init__(
        self,
        ready_pin: board.PIN,
        scl: board.PIN = board.SCL1,
        sda: board.PIN = board.SDA1,
    ) -> None:
        """
        Azoteq IQS5XX Trackpad Module Interface

        :param ready_pin: The pin to which the device's ready pin is connected
        :type ready_pin: board.PIN
        :param scl: The SCL pin for I2C communication (default is `board.SCL1`)
        :type scl: board.PIN, optional
        :param sda: The SDA pin for I2C communication (default is `board.SDA1`)
        :type sda: board.PIN, optional
        """
        self.ready_pin = ready_pin
        self.scl = scl
        self.sda = sda
        self.i2c = busio.I2C(self.scl, self.sda, frequency=I2C_FREQ)
        self.device = self._connect_device()

        # check if the connected device is really a ProxSense IQS5XX IC
        if self.product_no not in PRODUCT_NOS:
            raise RuntimeError(
                'This device is not recognized as an IQS5XX device'
            )

    def __getattr__(self, name: str):
        """
        Override to get the value of a register or class attribute

        :param name: The name of the attribute
        :type name: str

        :return: The value of the attribute
        :rtype: Any

        :raises AttributeError: IQS5XX has no attribute "<name>"
        """
        if name in REGISTERS.keys():  # get register value
            return self._get(name)
        elif name in self.__dict__:  # get class attribute value
            return self.__dict__[name]
        else:
            raise AttributeError(f'IQS5XX has no attribute "{name}"')

    def __setattr__(self, name: str, value) -> None:
        """
        Override to set the value of a register or class attribute

        :param name: The name of the attribute
        :type name: str
        :param value: The value to set
        :type value: Any

        :return: None

        :raises AttributeError: IQS5XX has no attribute "<name>"
        """
        if name in REGISTERS.keys():  # set register value
            self._set(name, value)
        elif name in self.__dict__:  # otherwise use standard __setattr__
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'IQS5XX has no attribute "{name}"')

    def _read_register(self, register: int, n_bytes: int = 1) -> bytearray:
        """
        Read data from a register

        :param register: The register address to read from
        :type register: int
        :param n_bytes: The number of bytes to read. Defaults to 1
        :type n_bytes: int, optional

        :return: The data read from the register as a bytearray, or an empty
                 bytearray if an OSError occurred
        :rtype: bytearray

        :raises OSError: If an error occurs during the read operation
        """
        try:
            # convert 16-bit address into byte-sized chunks
            register = self._addr_to_bytes(register)
            buffer = bytearray(n_bytes)
            with self.device:
                self.i2c.writeto_then_readfrom(DEVICE_ADDR, register, buffer)
        except OSError:  # FIXME: set up interrupt from IQS READY pin
            return bytearray()
        else:
            return buffer

    def _write_register(self, register: int, value: int) -> None:
        """
        Write data to a register

        :param register: The register address to write to.
        :type register: int
        :param value: The value to write to the register.
        :type value: int

        :return: None

        :raises OSError: If an error occurs during the write operation.
        """
        register = self._addr_to_bytes(register)
        with self.device:
            self.i2c.writeto(DEVICE_ADDR, register + bytes([value]))

    def _connect_device(self, timeout: float = 2.0) -> I2CDevice | None:
        """
        Attempt to connect to the device

        This method should only need to be called once at `__init__`

        NOTE from datasheet section 7.3.1 - I2C Wake:

        "The device can be woken from suspend by addressing it on the I2C bus.
        It will respond with a not-acknowledge (NACK) on the first addressing
        attempt and with an acknowledge (ACK) on the second addressing attempt,
        providing that there was at least a time difference of ~150us between
        the two addressing attempts. The suspend bit must then be disabled in
        that communication session to resume operations."

        :param timeout: Connection timeout in seconds. Default is 2 seconds
        :type timeout: float, optional

        :return: The device instance, or None if a timeout occurs
        :rtype: ~adafruit_bus_device.i2c_device.I2CDevice

        :raises TimeoutError: Could not connect to IQS5XX device
        """
        CONNECT_START = monotonic()
        while monotonic() < CONNECT_START + timeout:
            try:
                device = I2CDevice(self.i2c, DEVICE_ADDR)
            except ValueError:
                sleep(0.001)  # wait 1mS just to be safe
            else:
                # disable 'suspend' bit (bit 0 of system_control_1 register)
                register = self._addr_to_bytes(0x0432)
                with device:
                    self.wait_ready()
                    self.i2c.writeto(DEVICE_ADDR, register)
                return device
        else:
            raise TimeoutError('Could not connect to IQS5XX device')

    def _get(self, register_name: str) -> int:
        """
        Get the value stored in the given register

        :param register_name: The name of the register to read
        :type register_name: str

        :return: The value from the specified register as an int, or `0xFFFF`
                 if no data could be read
        :rtype: int

        :raises ValueError: Invalid register name "<register_name>"
        """
        hex_address, byte_length = REGISTERS.get(register_name, (None, None))

        if hex_address is None or byte_length is None:
            raise ValueError(f'Invalid register name "{register_name}"')

        self.wait_ready()

        if data := self._read_register(hex_address, byte_length):
            return int.from_bytes(data, 'big')  # return integer value
        return 0xFFFF

    def _set(self, register_name: str, new_value: int) -> None:
        """
        Set the value in the given register to new_val

        :param register_name: The name of the register to set
        :type register_name: str
        :param new_value: The value to set in the register
        :type new_value: int

        :return: None

        :raises ValueError: Invalid register name "<register_name>"
        """
        hex_address, _byte_length = REGISTERS.get(register_name, (None, None))

        if hex_address is None:
            raise ValueError(f'Invalid register name "{register_name}"')

        # if hex_address in range(0x0303, 0x06CE):
        #     warn(  # FIXME: warnings is broken?
        #         'Advanced feature register access is provided for '
        #         'completeness, and has not been fully tested/implemented'
        #     )
        # TODO: exception handling for invalid new value size (too many bytes)
        else:
            self.wait_ready()
            self._write_register(hex_address, new_value)

    def _addr_to_bytes(self, addr: int) -> bytes:
        """
        Convert the 16-bit register address value to two bytes

        :param addr: The 16-bit register address
        :type addr: int

        :return: The converted bytes
        :rtype: bytes
        """
        return bytes([addr >> 8, addr & 0xFF])

    def _end_session(self) -> None:
        """
        Send the "End Communication Window" command by writing to `0xEEEE`

        :return: None
        """
        register = self._addr_to_bytes(0xEEEE)
        try:
            with self.device:
                self.wait_ready()
                self.i2c.writeto(DEVICE_ADDR, register + bytes([0]))
                sleep(0.01)
        except OSError:
            return

    def get_gesture(self) -> str | None:
        """
        Return the name of the detected gesture, or None if no gesture was
        detected

        Possible gesture names:
        - 'SINGLE_TAP'
        - 'PRESS_AND_HOLD'
        - 'SWIPE_RIGHT'
        - 'SWIPE_LEFT'
        - 'SWIPE_UP'
        - 'SWIPE_DOWN'
        - 'TWO_FINGER_TAP'
        - 'SCROLL'
        - 'ZOOM'

        :return: The name of the detected gesture
        :rtype: str | None
        """
        g0 = self._get('gesture_events_0')  # single-finger gestures
        g1 = self._get('gesture_events_1')  # two-finger gestures
        # get the aggregate gesture flags by inserting the bits from the
        # gesture_events_1 register as the 3 upper bits, then mask with 0x1FF
        # to ensure the value is 9 bits wide
        gesture_flags = ((g1 << 6) | g0) & 0x1FF
        return GESTURE_EVENTS.get(gesture_flags, None)

    def wait_ready(self) -> None:
        """
        Wait for a rising edge on the `ready_pin`

        :return: None
        """
        with Counter(self.ready_pin, edge=Edge.RISE) as interrupt:
            # use a Counter on the RDY pin as an interrupt for reading data
            while interrupt.count < 0:
                pass
            else:
                # interrupt.reset()  # REVIEW: is there a difference here?
                interrupt.count = 0
