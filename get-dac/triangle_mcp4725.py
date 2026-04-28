import machine
import math
import time

AMPLITUDE = 2047
FREQUENCY = 100
SAMPLE_RATE = 10000

i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))

MCP4725_ADDR = 0x60

def set_dac_value(value):
    value = max(0, min(4095, value))
    data = bytearray([(value >> 4) & 0xFF, (value << 4) & 0xFF])
    i2c.writeto(MCP4725_ADDR, data)

def generate_triangle():
    samples_per_period = SAMPLE_RATE // FREQUENCY
    step = (2 * AMPLITUDE) / (samples_per_period // 2)
    
    while True:
        for i in range(samples_per_period // 2):
            value = int(2047 + i * step)
            set_dac_value(value)
            time.sleep_us(1_000_000 // SAMPLE_RATE)
        
        for i in range(samples_per_period // 2):
            value = int(2047 + AMPLITUDE - i * step)
            set_dac_value(value)
            time.sleep_us(1_000_000 // SAMPLE_RATE)

generate_triangle()