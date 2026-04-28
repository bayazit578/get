import machine
import math
import time

AMPLITUDE = 127
FREQUENCY = 100
SAMPLE_RATE = 10000

dac_pins = [machine.Pin(i, machine.Pin.OUT) for i in range(8)]

def set_dac_value(value):
    for i in range(8):
        dac_pins[i].value((value >> i) & 1)

def generate_triangle():
    samples_per_period = SAMPLE_RATE // FREQUENCY
    step = (2 * AMPLITUDE) / (samples_per_period // 2)
    
    while True:
        for i in range(samples_per_period // 2):
            value = int(127 + i * step)
            set_dac_value(max(0, min(255, value)))
            time.sleep_us(1_000_000 // SAMPLE_RATE)
        
        for i in range(samples_per_period // 2):
            value = int(127 + AMPLITUDE - i * step)
            set_dac_value(max(0, min(255, value)))
            time.sleep_us(1_000_000 // SAMPLE_RATE)

generate_triangle()