# IQS5XX
Version 0.1.1

CircuitPython library for Azoteq IQS5XX trackpad modules, the TPS43 and TPS65 (see datasheet below)

## Basic Usage
### Software
1. copy `iqs5xx.py` to the `lib` dir on your `CIRCUITPY` drive (or use the precompiled `iqs5xx.mpy` instead if you're tight on space!)
3. copy `main.py` from `examples/main.py` to the root of your `CIRCUITPY` drive
4. view output via the CircuitPython REPL / serial monitor
### Hardware
1. connect the `GND`, `3V3`, `SDA` and `SCL` pins from the trackpad module to the microcontroller via a [STEMMA QT to male header cable](https://www.adafruit.com/product/4209) or similar
2. connect the `RDY` pin from the trackpad module to an interrupt-capable pin on the microcontroller - On the QTPy RP2040 this is any pin in PWM group "B"; `MOSI` is used in the example `main.py` file

This library has been tested on:
- [CircutPython 8.2.9](https://circuitpython.org/board/adafruit_qtpy_rp2040/)
- [Adafruit QT Py RP2040 microcontroller](https://www.adafruit.com/product/4900)

It *should* work on other CircuitPython-compatible hardware, but YMMV - this library is a work in progress! Contributions are welcome.

## Hardware Info
#### Azoteq hardware[^1]
[TPS43/TPS65 trackpad module datasheet](https://www.mouser.com/datasheet/2/42/proxsense_i2c_trackpad_datasheet-1626845.pdf)

[Azoteq IQS5XX "ProxSense&reg;" series datasheet](https://www.azoteq.com/images/stories/pdf/iqs5xx-b000_trackpad_datasheet.pdf)

[^1]: All trademarks are property of their respective owners
