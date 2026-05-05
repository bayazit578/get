#!/usr/bin/env python3
from mcp4725_driver import MCP4725
import signal_generator as sg
import time

amplitude = 3.2
signal_freq = 10
sampling_freq = 1000

try:
    mcp4725 = MCP4725(5.11, 0x61, True)
    while True:
        mcp4725.set_voltage(amplitude * sg.get_sin_wave_amplitude(signal_freq, time.monotonic()))
        sg.wait_for_sampling_period(sampling_freq)
finally:
    mcp4725.deinit()
