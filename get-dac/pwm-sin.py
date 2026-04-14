import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = float(input("Введите амплитуду сигнала (0-3.3 В): "))
signal_frequency = float(input("Введите частоту сигнала (Гц): "))
sampling_frequency = float(input("Введите частоту дискретизации (Гц): "))

dac = None

try:
    dac = pwm.PWM_DAC(12, 500, 3.3, False)
    
    start_time = time.time()
    
    while True:
        current_time = time.time() - start_time
        normalized_amplitude = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_amplitude * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    pass

finally:
    if dac:
        dac.deinit()
