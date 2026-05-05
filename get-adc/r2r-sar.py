#!/bin/env python3

import r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

try:
    max_voltage = 3.294
    adc = R2R_ADC(max_voltage)
    v = []
    t = []
    duration = 3.0
    start = time.monotonic()
    moment_time = start
    while moment_time - start < duration:
        v.append(adc.get_sar_voltage())
        t.append(moment_time)
        moment_time = time.monotonic()
    plot_voltage_vs_time(t, v, max_voltage)
    plot_sampling_period_hist(t)
finally:
    adc.deinit()
