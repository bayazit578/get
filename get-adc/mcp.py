#!/usr/bin/env python3
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist
import time

max_voltage = 5.22

mcp = MCP3021(max_voltage)
try:
    v = []
    t = []
    duration = 3.0
    start = time.monotonic()
    now = start
    while now - start < duration:
        v.append(mcp.get_voltage())
        t.append(now - start)
        now = time.monotonic()
    plot_voltage_vs_time(t, v, max_voltage)
    plot_sampling_period_hist(t)
finally:
    mcp.deinit()
