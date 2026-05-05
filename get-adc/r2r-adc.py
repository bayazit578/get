#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.compare_time = compare_time
        self.verbose = verbose

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    
    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    
    def number_to_dac(self, number):
        if not (0 <= number <= 255):
            print("Out of range [0, 255]")
            return
        a = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, a)
    
    def sequential_counting_adc(self):
        for value in range(256):
            self.number_to_dac(value)
            time.sleep(self.compare_time)
            comp_value = GPIO.input(self.comp_gpio)
            print(comp_value)
            if comp_value == 1:
                return value
        return 255
    
    def get_sc_voltage(self):
        voltage = self.sequential_counting_adc() / 255 * self.dynamic_range
        return voltage
    
    def successive_approximation_adc(self):
        result = 0
        for i in range(7, -1, -1):
            w  = 1 << i
            self.number_to_dac(result + w)
            time.sleep(self.compare_time)
            if not GPIO.input(self.comp_gpio):
                result += w
        return result

    def get_sar_voltage(self):
        return self.successive_approximation_adc() / 255 * self.dynamic_range

if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.294, 0.01, True)

        while True:
            print(f"Напряжение: {adc.get_sc_voltage():.02f}")
    finally:
        adc.deinit()
