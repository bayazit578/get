import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

dac = None

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, False)
    
    start_time = time.time()
    half_period = 1 / (2 * signal_frequency)
    
    while True:
        current_time = time.time() - start_time
        
        period_position = current_time % (1 / signal_frequency)
        
        if period_position < half_period:
            voltage = 2 * amplitude * period_position * signal_frequency
        else:
            voltage = 2 * amplitude * (1 - period_position * signal_frequency)
        
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    pass

finally:
    if dac:
        dac.deinit()