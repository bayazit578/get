#!/bin/env python3

from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time
import time

adc = R2R_ADC(2.294, 0.0001, True)

voltage_values = []
time_values = []
duration = 3.0

try:
    start_time = time.monotonic()
    moment_time = time.monotonic()
    while (moment_time - start_time < duration):
        voltage_values.append(adc.get_sc_voltage())
        time_values.append(moment_time - start_time)
        print(adc.get_sc_voltage(), moment_time - start_time)
        moment_time = time.monotonic()
    plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
finally:
    adc.deinit()
