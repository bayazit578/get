import machine
import math
import time

AMPLITUDE = 127
FREQUENCY = 100
SAMPLE_RATE = 10000

pwm_pin = machine.Pin(0, machine.Pin.OUT)
pwm = machine.PWM(pwm_pin)
pwm.freq(100000)

def set_pwm_value(value):
    duty = int((value / 255) * 1023)
    pwm.duty(duty)

def generate_triangle():
    samples_per_period = SAMPLE_RATE // FREQUENCY
    step = (2 * AMPLITUDE) / (samples_per_period // 2)
    
    while True:
        for i in range(samples_per_period // 2):
            value = int(127 + i * step)
            set_pwm_value(max(0, min(255, value)))
            time.sleep_us(1_000_000 // SAMPLE_RATE)
        
        for i in range(samples_per_period // 2):
            value = int(127 + AMPLITUDE - i * step)
            set_pwm_value(max(0, min(255, value)))
            time.sleep_us(1_000_000 // SAMPLE_RATE)

generate_triangle()