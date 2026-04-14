import numpy as np
import time

def get_sin_wave_amplitude(freq, time_moment):
    amplitude_raw = np.sin(2 * np.pi * freq * time_moment)
    amplitude_shifted = amplitude_raw + 1
    amplitude_normalized = amplitude_shifted / 2
    return amplitude_normalized

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)
