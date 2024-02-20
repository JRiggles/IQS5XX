# region - property definitions for all registers
# create properties for each register value for easier access
# @property
# def device_id(self) -> int:
#     return self._get('device_id')

# @property
# def product_no(self) -> int:
#     return self._get('product_no')

# @property
# def project_no(self) -> int:
#     return self._get('project_no')

# @property
# def major_version(self) -> int:
#     return self._get('major_version')

# @property
# def minor_version(self) -> int:
#     return self._get('minor_version')

# @property
# def bootloader_status(self) -> int:
#     return self._get('bootloader_status')

# @property
# def max_touch_info(self) -> int:
#     return self._get('max_touch_info')

# @property
# def previous_cycle_time(self) -> int:
#     return self._get('previous_cycle_time')

# @property
# def gesture_events_0(self) -> int:
#     return self._get('gesture_events_0')

# @property
# def gesture_events_1(self) -> int:
#     return self._get('gesture_events_1')

# @property
# def system_info_0(self) -> int:
#     return self._get('system_info_0')

# @property
# def system_info_1(self) -> int:
#     return self._get('system_info_1')

# @property
# def n_fingers(self) -> int:
#     return self._get('n_fingers')

# @property
# def relative_x(self) -> int:
#     return self._get('relative_x')

# @property
# def relative_y(self) -> int:
#     return self._get('relative_y')

# @property
# def absolute_x(self) -> int:
#     return self._get('absolute_x')

# @property
# def absolute_x_1(self) -> int:
#     # functionally the same as 'absolute_x'
#     return self._get('absolute_x', finger=1)

# @property
# def absolute_x_2(self) -> int:
#     return self._get('absolute_x', finger=2)

# @property
# def absolute_x_3(self) -> int:
#     return self._get('absolute_x', finger=3)

# @property
# def absolute_x_4(self) -> int:
#     return self._get('absolute_x', finger=4)

# @property
# def absolute_x_5(self) -> int:
#     return self._get('absolute_x', finger=5)

# @property
# def absolute_y(self) -> int:
#     return self._get('absolute_y')

# @property
# def absolute_y_1(self) -> int:
#     # functionally the same as 'absolute_y'
#     return self._get('absolute_y', finger=1)

# @property
# def absolute_y_2(self) -> int:
#     return self._get('absolute_y', finger=2)

# @property
# def absolute_y_3(self) -> int:
#     return self._get('absolute_y', finger=3)

# @property
# def absolute_y_4(self) -> int:
#     return self._get('absolute_y', finger=4)

# @property
# def absolute_y_5(self) -> int:
#     return self._get('absolute_y', finger=5)

# @property
# def touch_strength(self) -> int:
#     return self._get('touch_strength')

# @property
# def touch_strength_1(self) -> int:
#     # functionally the same as 'touch_strength'
#     return self._get('touch_strength', finger=1)

# @property
# def touch_strength_2(self) -> int:
#     return self._get('touch_strength', finger=2)

# @property
# def touch_strength_3(self) -> int:
#     return self._get('touch_strength', finger=3)

# @property
# def touch_strength_4(self) -> int:
#     return self._get('touch_strength', finger=4)

# @property
# def touch_strength_5(self) -> int:
#     return self._get('touch_strength', finger=5)

# @property
# def touch_areasize(self) -> int:
#     return self._get('touch_areasize')

# @property
# def touch_areasize_1(self) -> int:
#     # functionally the same as 'touch_areasize'
#     return self._get('touch_areasize', finger=1)

# @property
# def touch_areasize_2(self) -> int:
#     return self._get('touch_areasize', finger=2)

# @property
# def touch_areasize_3(self) -> int:
#     return self._get('touch_areasize', finger=3)

# @property
# def touch_areasize_4(self) -> int:
#     return self._get('touch_areasize', finger=4)

# @property
# def touch_areasize_5(self) -> int:
#     return self._get('touch_areasize', finger=5)

# @property
# def prox_status(self) -> int:
#     return self._get('prox_status')

# @property
# def touch_status(self) -> int:
#     return self._get('touch_status')

# @property
# def snap_status(self) -> int:
#     return self._get('snap_status')

# @property
# def count_values(self) -> int:
#     return self._get('count_values')

# @property
# def delta_values(self) -> int:
#     return self._get('delta_values')

# @property
# def alp_count_value(self) -> int:
#     return self._get('alp_count_value')

# @property
# def alp_individual_count_values(self) -> int:
#     return self._get('alp_individual_count_values')

# # ---- ADVANCED FEATURE REGISTERS ----
# # NOTE: the registers below are read/write
# @property
# def reference_values(self) -> int:
#     return self._get('reference_values')

# @reference_values.setter
# def reference_values(self, new_value: int) -> None:
#     self._set('reference_values', new_value)

# @property
# def alp_lta(self) -> int:
#     return self._get('alp_lta')

# @alp_lta.setter
# def alp_lta(self, new_value: int) -> None:
#     self._set('alp_lta', new_value)

# @property
# def system_control_0(self) -> int:
#     return self._get('system_control_0')

# @system_control_0.setter
# def system_control_0(self, new_value: int) -> None:
#     self._set('system_control_0', new_value)

# @property
# def system_control_1(self) -> int:
#     return self._get('system_control_1')

# @system_control_1.setter
# def system_control_1(self, new_value: int) -> None:
#     self._set('system_control_1', new_value)

# @property
# def alp_ati_compensation(self) -> int:
#     return self._get('alp_ati_compensation')

# @alp_ati_compensation.setter
# def alp_ati_compensation(self, new_value: int) -> None:
#     self._set('alp_ati_compensation', new_value)

# @property
# def ati_compensation(self) -> int:
#     return self._get('ati_compensation')

# @ati_compensation.setter
# def ati_compensation(self, new_value: int) -> None:
#     self._set('ati_compensation', new_value)

# @property
# def ati_c_individual_adjust(self) -> int:
#     return self._get('ati_c_individual_adjust')

# @ati_c_individual_adjust.setter
# def ati_c_individual_adjust(self, new_value: int) -> None:
#     self._set('ati_c_individual_adjust', new_value)

# @property
# def global_ati_c(self) -> int:
#     return self._get('global_ati_c')

# @global_ati_c.setter
# def global_ati_c(self, new_value: int) -> None:
#     self._set('global_ati_c', new_value)

# @property
# def alp_ati_c(self) -> int:
#     return self._get('alp_ati_c')

# @alp_ati_c.setter
# def alp_ati_c(self, new_value: int) -> None:
#     self._set('alp_ati_c', new_value)

# @property
# def ati_target(self) -> int:
#     return self._get('ati_target')

# @ati_target.setter
# def ati_target(self, new_value: int) -> None:
#     self._set('ati_target', new_value)

# @property
# def alp_ati_target(self) -> int:
#     return self._get('alp_ati_target')

# @alp_ati_target.setter
# def alp_ati_target(self, new_value: int) -> None:
#     self._set('alp_ati_target', new_value)

# @property
# def reference_drift_limit(self) -> int:
#     return self._get('reference_drift_limit')

# @reference_drift_limit.setter
# def reference_drift_limit(self, new_value: int) -> None:
#     self._set('reference_drift_limit', new_value)

# @property
# def alp_lta_drift_limit(self) -> int:
#     return self._get('alp_lta_drift_limit')

# @alp_lta_drift_limit.setter
# def alp_lta_drift_limit(self, new_value: int) -> None:
#     self._set('alp_lta_drift_limit', new_value)

# @property
# def re_ati_upper_compensation_limit(self) -> int:
#     return self._get('re_ati_upper_compensation_limit')

# @re_ati_upper_compensation_limit.setter
# def re_ati_upper_compensation_limit(self, new_value: int) -> None:
#     self._set('re_ati_upper_compensation_limit', new_value)

# @property
# def max_count_limit(self) -> int:
#     return self._get('max_count_limit')

# @max_count_limit.setter
# def max_count_limit(self, new_value: int) -> None:
#     self._set('max_count_limit', new_value)

# @property
# def re_ati_retry_time_s(self) -> int:
#     return self._get('re_ati_retry_time_s')

# @re_ati_retry_time_s.setter
# def re_ati_retry_time_s(self, new_value: int) -> None:
#     self._set('re_ati_retry_time_s', new_value)

# @property
# def report_rate_active_mode_ms(self) -> int:
#     return self._get('report_rate_active_mode_ms')

# @report_rate_active_mode_ms.setter
# def report_rate_active_mode_ms(self, new_value: int) -> None:
#     self._set('report_rate_active_mode_ms', new_value)

# @property
# def report_rate_idle_touch_mode_ms(self) -> int:
#     return self._get('report_rate_idle_touch_mode_ms')

# @report_rate_idle_touch_mode_ms.setter
# def report_rate_idle_touch_mode_ms(self, new_value: int) -> None:
#     self._set('report_rate_idle_touch_mode_ms', new_value)

# @property
# def report_rate_idle_mode_ms(self) -> int:
#     return self._get('report_rate_idle_mode_ms')

# @report_rate_idle_mode_ms.setter
# def report_rate_idle_mode_ms(self, new_value: int) -> None:
#     self._set('report_rate_idle_mode_ms', new_value)

# @property
# def report_rate_lp1_mode_ms(self) -> int:
#     return self._get('report_rate_lp1_mode_ms')

# @report_rate_lp1_mode_ms.setter
# def report_rate_lp1_mode_ms(self, new_value: int) -> None:
#     self._set('report_rate_lp1_mode_ms', new_value)

# @property
# def report_rate_lp2_mode_ms(self) -> int:
#     return self._get('report_rate_lp2_mode_ms')

# @report_rate_lp2_mode_ms.setter
# def report_rate_lp2_mode_ms(self, new_value: int) -> None:
#     self._set('report_rate_lp2_mode_ms', new_value)

# @property
# def timeout_active_mode_s(self) -> int:
#     return self._get('timeout_active_mode_s')

# @timeout_active_mode_s.setter
# def timeout_active_mode_s(self, new_value: int) -> None:
#     self._set('timeout_active_mode_s', new_value)

# @property
# def timeout_idle_touch_mode_s(self) -> int:
#     return self._get('timeout_idle_touch_mode_s')

# @timeout_idle_touch_mode_s.setter
# def timeout_idle_touch_mode_s(self, new_value: int) -> None:
#     self._set('timeout_idle_touch_mode_s', new_value)

# @property
# def timeout_idle_mode_s(self) -> int:
#     return self._get('timeout_idle_mode_s')

# @timeout_idle_mode_s.setter
# def timeout_idle_mode_s(self, new_value: int) -> None:
#     self._set('timeout_idle_mode_s', new_value)

# @property
# def timeout_lp1_mode_x20s(self) -> int:
#     return self._get('timeout_lp1_mode_x20s')

# @timeout_lp1_mode_x20s.setter
# def timeout_lp1_mode_x20s(self, new_value: int) -> None:
#     self._set('timeout_lp1_mode_x20s', new_value)

# @property
# def reference_update_time_s(self) -> int:
#     return self._get('reference_update_time_s')

# @reference_update_time_s.setter
# def reference_update_time_s(self, new_value: int) -> None:
#     self._set('reference_update_time_s', new_value)

# @property
# def snap_timeout_s(self) -> int:
#     return self._get('snap_timeout_s')

# @snap_timeout_s.setter
# def snap_timeout_s(self, new_value: int) -> None:
#     self._set('snap_timeout_s', new_value)

# @property
# def i2c_timeout_ms(self) -> int:
#     return self._get('i2c_timeout_ms')

# @i2c_timeout_ms.setter
# def i2c_timeout_ms(self, new_value: int) -> None:
#     self._set('i2c_timeout_ms', new_value)

# @property
# def system_config_0(self) -> int:
#     return self._get('system_config_0')

# @system_config_0.setter
# def system_config_0(self, new_value: int) -> None:
#     self._set('system_config_0', new_value)

# @property
# def system_config_1(self) -> int:
#     return self._get('system_config_1')

# @system_config_1.setter
# def system_config_1(self, new_value: int) -> None:
#     self._set('system_config_1', new_value)

# @property
# def snap_threshold(self) -> int:
#     return self._get('snap_threshold')

# @snap_threshold.setter
# def snap_threshold(self, new_value: int) -> None:
#     self._set('snap_threshold', new_value)

# @property
# def prox_threshold_trackpad(self) -> int:
#     return self._get('prox_threshold_trackpad')

# @prox_threshold_trackpad.setter
# def prox_threshold_trackpad(self, new_value: int) -> None:
#     self._set('prox_threshold_trackpad', new_value)

# @property
# def prox_threshold_alp_channel(self) -> int:
#     return self._get('prox_threshold_alp_channel')

# @prox_threshold_alp_channel.setter
# def prox_threshold_alp_channel(self, new_value: int) -> None:
#     self._set('prox_threshold_alp_channel', new_value)

# @property
# def global_touch_multiplier_set(self) -> int:
#     return self._get('global_touch_multiplier_set')

# @global_touch_multiplier_set.setter
# def global_touch_multiplier_set(self, new_value: int) -> None:
#     self._set('global_touch_multiplier_set', new_value)
# # ... (previous properties)

# @property
# def global_touch_multiplier_clear(self) -> int:
#     return self._get('global_touch_multiplier_clear')

# @global_touch_multiplier_clear.setter
# def global_touch_multiplier_clear(self, new_value: int) -> None:
#     self._set('global_touch_multiplier_clear', new_value)

# @property
# def individual_touch_multiplier_adjustments(self) -> int:
#     return self._get('individual_touch_multiplier_adjustments')

# @individual_touch_multiplier_adjustments.setter
# def individual_touch_multiplier_adjustments(self, new_value: int) -> None:
#     self._set('individual_touch_multiplier_adjustments', new_value)

# @property
# def minimum_count_re_ati_delta(self) -> int:
#     return self._get('minimum_count_re_ati_delta')

# @minimum_count_re_ati_delta.setter
# def minimum_count_re_ati_delta(self, new_value: int) -> None:
#     self._set('minimum_count_re_ati_delta', new_value)

# @property
# def filter_settings_0(self) -> int:
#     return self._get('filter_settings_0')

# @filter_settings_0.setter
# def filter_settings_0(self, new_value: int) -> None:
#     self._set('filter_settings_0', new_value)

# @property
# def xy_static_beta(self) -> int:
#     return self._get('xy_static_beta')

# @xy_static_beta.setter
# def xy_static_beta(self, new_value: int) -> None:
#     self._set('xy_static_beta', new_value)

# @property
# def alp_count_beta(self) -> int:
#     return self._get('alp_count_beta')

# @alp_count_beta.setter
# def alp_count_beta(self, new_value: int) -> None:
#     self._set('alp_count_beta', new_value)

# @property
# def alp1_lta_beta(self) -> int:
#     return self._get('alp1_lta_beta')

# @alp1_lta_beta.setter
# def alp1_lta_beta(self, new_value: int) -> None:
#     self._set('alp1_lta_beta', new_value)

# # ... (previous properties)

# @property
# def alp2_lta_beta(self) -> int:
#     return self._get('alp2_lta_beta')

# @alp2_lta_beta.setter
# def alp2_lta_beta(self, new_value: int) -> None:
#     self._set('alp2_lta_beta', new_value)

# @property
# def xy_dynamic_filter_bottom_beta(self) -> int:
#     return self._get('xy_dynamic_filter_bottom_beta')

# @xy_dynamic_filter_bottom_beta.setter
# def xy_dynamic_filter_bottom_beta(self, new_value: int) -> None:
#     self._set('xy_dynamic_filter_bottom_beta', new_value)

# @property
# def xy_dynamic_filter_lower_speed(self) -> int:
#     return self._get('xy_dynamic_filter_lower_speed')

# @xy_dynamic_filter_lower_speed.setter
# def xy_dynamic_filter_lower_speed(self, new_value: int) -> None:
#     self._set('xy_dynamic_filter_lower_speed', new_value)

# @property
# def xy_dynamic_filter_upper_speed(self) -> int:
#     return self._get('xy_dynamic_filter_upper_speed')

# @xy_dynamic_filter_upper_speed.setter
# def xy_dynamic_filter_upper_speed(self, new_value: int) -> None:
#     self._set('xy_dynamic_filter_upper_speed', new_value)

# @property
# def total_rx(self) -> int:
#     return self._get('total_rx')

# @total_rx.setter
# def total_rx(self, new_value: int) -> None:
#     self._set('total_rx', new_value)

# @property
# def total_tx(self) -> int:
#     return self._get('total_tx')

# @total_tx.setter
# def total_tx(self, new_value: int) -> None:
#     self._set('total_tx', new_value)

# @property
# def rx_mapping(self) -> bytearray:
#     return self._get('rx_mapping', as_bytearray=True)

# @rx_mapping.setter
# def rx_mapping(self, new_value: int) -> None:
#     self._set('rx_mapping', new_value)

# @property
# def tx_mapping(self) -> bytearray:
#     return self._get('tx_mapping', as_bytearray=True)

# @tx_mapping.setter
# def tx_mapping(self, new_value: int) -> None:
#     self._set('tx_mapping', new_value)

# @property
# def alp_channel_setup_0(self) -> int:
#     return self._get('alp_channel_setup_0')

# @alp_channel_setup_0.setter
# def alp_channel_setup_0(self, new_value: int) -> None:
#     self._set('alp_channel_setup_0', new_value)

# @property
# def alp_rx_select(self) -> int:
#     return self._get('alp_rx_select')

# @alp_rx_select.setter
# def alp_rx_select(self, new_value: int) -> None:
#     self._set('alp_rx_select', new_value)

# @property
# def alp_tx_select(self) -> int:
#     return self._get('alp_tx_select')

# @alp_tx_select.setter
# def alp_tx_select(self, new_value: int) -> None:
#     self._set('alp_tx_select', new_value)

# # ... (previous properties)

# @property
# def rx_to_tx(self) -> int:
#     return self._get('rx_to_tx')

# @rx_to_tx.setter
# def rx_to_tx(self, new_value: int) -> None:
#     self._set('rx_to_tx', new_value)

# @property
# def hardware_settings_a(self) -> int:
#     return self._get('hardware_settings_a')

# @hardware_settings_a.setter
# def hardware_settings_a(self, new_value: int) -> None:
#     self._set('hardware_settings_a', new_value)

# @property
# def hardware_settings_b1(self) -> int:
#     return self._get('hardware_settings_b1')

# @hardware_settings_b1.setter
# def hardware_settings_b1(self, new_value: int) -> None:
#     self._set('hardware_settings_b1', new_value)

# @property
# def hardware_settings_b2_alp(self) -> int:
#     return self._get('hardware_settings_b2_alp')

# @hardware_settings_b2_alp.setter
# def hardware_settings_b2_alp(self, new_value: int) -> None:
#     self._set('hardware_settings_b2_alp', new_value)

# @property
# def hardware_settings_c1(self) -> int:
#     return self._get('hardware_settings_c1')

# @hardware_settings_c1.setter
# def hardware_settings_c1(self, new_value: int) -> None:
#     self._set('hardware_settings_c1', new_value)

# @property
# def hardware_settings_c2_alp(self) -> int:
#     return self._get('hardware_settings_c2_alp')

# @hardware_settings_c2_alp.setter
# def hardware_settings_c2_alp(self, new_value: int) -> None:
#     self._set('hardware_settings_c2_alp', new_value)

# @property
# def hardware_settings_d1(self) -> int:
#     return self._get('hardware_settings_d1')

# @hardware_settings_d1.setter
# def hardware_settings_d1(self, new_value: int) -> None:
#     self._set('hardware_settings_d1', new_value)

# @property
# def hardware_settings_d2_alp(self) -> int:
#     return self._get('hardware_settings_d2_alp')

# @hardware_settings_d2_alp.setter
# def hardware_settings_d2_alp(self, new_value: int) -> None:
#     self._set('hardware_settings_d2_alp', new_value)

# @property
# def xy_config_0(self) -> int:
#     return self._get('xy_config_0')

# @xy_config_0.setter
# def xy_config_0(self, new_value: int) -> None:
#     self._set('xy_config_0', new_value)

# @property
# def max_multi_touches(self) -> int:
#     return self._get('max_multi_touches')

# @max_multi_touches.setter
# def max_multi_touches(self, new_value: int) -> None:
#     self._set('max_multi_touches', new_value)

# @property
# def finger_split_aggression_factor(self) -> int:
#     return self._get('finger_split_aggression_factor')

# @finger_split_aggression_factor.setter
# def finger_split_aggression_factor(self, new_value: int) -> None:
#     self._set('finger_split_aggression_factor', new_value)

# @property
# def palm_reject_threshold(self) -> int:
#     return self._get('palm_reject_threshold')

# @palm_reject_threshold.setter
# def palm_reject_threshold(self, new_value: int) -> None:
#     self._set('palm_reject_threshold', new_value)

# @property
# def palm_reject_timeout_x_32ms(self) -> int:
#     return self._get('palm_reject_timeout_x_32ms')

# @palm_reject_timeout_x_32ms.setter
# def palm_reject_timeout_x_32ms(self, new_value: int) -> None:
#     self._set('palm_reject_timeout_x_32ms', new_value)

# @property
# def x_resolution_px(self) -> int:
#     return self._get('x_resolution_px')

# @x_resolution_px.setter
# def x_resolution_px(self, new_value: int) -> None:
#     self._set('x_resolution_px', new_value)

# @property
# def y_resolution_px(self) -> int:
#     return self._get('y_resolution_px')

# @y_resolution_px.setter
# def y_resolution_px(self, new_value: int) -> None:
#     self._set('y_resolution_px', new_value)

# @property
# def stationary_touch_movement_threshold_px(self) -> int:
#     return self._get('stationary_touch_movement_threshold_px')

# @stationary_touch_movement_threshold_px.setter
# def stationary_touch_movement_threshold_px(self, new_value: int) -> None:
#     self._set('stationary_touch_movement_threshold_px', new_value)

# @property
# def default_read_address(self) -> int:
#     return self._get('default_read_address')

# @default_read_address.setter
# def default_read_address(self, new_value: int) -> None:
#     self._set('default_read_address', new_value)

# @property
# def export_file_version_number(self) -> int:
#     return self._get('export_file_version_number')

# @export_file_version_number.setter
# def export_file_version_number(self, new_value: int) -> None:
#     self._set('export_file_version_number', new_value)

# @property
# def prox_debounce(self) -> int:
#     return self._get('prox_debounce')

# @prox_debounce.setter
# def prox_debounce(self, new_value: int) -> None:
#     self._set('prox_debounce', new_value)

# @property
# def touch_snap_debounce(self) -> int:
#     return self._get('touch_snap_debounce')

# @touch_snap_debounce.setter
# def touch_snap_debounce(self, new_value: int) -> None:
#     self._set('touch_snap_debounce', new_value)

# @property
# def active_channels(self) -> bytearray:
#     return self._get('active_channels', as_bytearray=True)

# @active_channels.setter
# def active_channels(self, new_value: int) -> None:
#     self._set('active_channels', new_value)

# @property
# def snap_enabled_channels(self) -> bytearray:
#     return self._get('snap_enabled_channels', as_bytearray=True)

# @snap_enabled_channels.setter
# def snap_enabled_channels(self, new_value: int) -> None:
#     self._set('snap_enabled_channels', new_value)

# @property
# def single_finger_gestures(self) -> int:
#     return self._get('single_finger_gestures')

# @single_finger_gestures.setter
# def single_finger_gestures(self, new_value: int) -> None:
#     self._set('single_finger_gestures', new_value)

# @property
# def multi_finger_gestures(self) -> int:
#     return self._get('multi_finger_gestures')

# @multi_finger_gestures.setter
# def multi_finger_gestures(self, new_value: int) -> None:
#     self._set('multi_finger_gestures', new_value)

# @property
# def tap_time_ms(self) -> int:
#     return self._get('tap_time_ms')

# @tap_time_ms.setter
# def tap_time_ms(self, new_value: int) -> None:
#     self._set('tap_time_ms', new_value)

# @property
# def tap_distance_px(self) -> int:
#     return self._get('tap_distance_px')

# @tap_distance_px.setter
# def tap_distance_px(self, new_value: int) -> None:
#     self._set('tap_distance_px', new_value)

# @property
# def hold_time_ms(self) -> int:
#     return self._get('hold_time_ms')

# @hold_time_ms.setter
# def hold_time_ms(self, new_value: int) -> None:
#     self._set('hold_time_ms', new_value)

# @property
# def swipe_initial_time_ms(self) -> int:
#     return self._get('swipe_initial_time_ms')

# @swipe_initial_time_ms.setter
# def swipe_initial_time_ms(self, new_value: int) -> None:
#     self._set('swipe_initial_time_ms', new_value)

# @property
# def swipe_initial_distance_px(self) -> int:
#     return self._get('swipe_initial_distance_px')

# @swipe_initial_distance_px.setter
# def swipe_initial_distance_px(self, new_value: int) -> None:
#     self._set('swipe_initial_distance_px', new_value)

# @property
# def swipe_consecutive_time_ms(self) -> int:
#     return self._get('swipe_consecutive_time_ms')

# @swipe_consecutive_time_ms.setter
# def swipe_consecutive_time_ms(self, new_value: int) -> None:
#     self._set('swipe_consecutive_time_ms', new_value)

# @property
# def swipe_consecutive_distance_px(self) -> int:
#     return self._get('swipe_consecutive_distance_px')

# @swipe_consecutive_distance_px.setter
# def swipe_consecutive_distance_px(self, new_value: int) -> None:
#     self._set('swipe_consecutive_distance_px', new_value)

# @property
# def swipe_angle(self) -> int:
#     return self._get('swipe_angle')

# @swipe_angle.setter
# def swipe_angle(self, new_value: int) -> None:
#     self._set('swipe_angle', new_value)

# @property
# def scroll_initial_distance_px(self) -> int:
#     return self._get('scroll_initial_distance_px')

# @scroll_initial_distance_px.setter
# def scroll_initial_distance_px(self, new_value: int) -> None:
#     self._set('scroll_initial_distance_px', new_value)

# @property
# def scroll_angle(self) -> int:
#     return self._get('scroll_angle')

# @scroll_angle.setter
# def scroll_angle(self, new_value: int) -> None:
#     self._set('scroll_angle', new_value)

# @property
# def zoom_initial_distance_px(self) -> int:
#     return self._get('zoom_initial_distance_px')

# @zoom_initial_distance_px.setter
# def zoom_initial_distance_px(self, new_value: int) -> None:
#     self._set('zoom_initial_distance_px', new_value)

# @property
# def zoom_consecutive_distance_px(self) -> int:
#     return self._get('zoom_consecutive_distance_px')

# @zoom_consecutive_distance_px.setter
# def zoom_consecutive_distance_px(self, new_value: int) -> None:
#     self._set('zoom_consecutive_distance_px', new_value)
# endregion
