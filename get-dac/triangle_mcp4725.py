import smbus
import signal_generator as sg
import time

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose=False):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.wm = 0x00
        self.pds = 0x00
        self.verbose = verbose
        self.dynamic_range = dynamic_range
    
    def deinit(self):
        self.bus.close()
    
    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return
        
        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4725 (12 бит)")
            return
        
        first_byte = self.wm | self.pds | (number >> 8)
        second_byte = number & 0xFF
        self.bus.write_byte_data(self.address, first_byte, second_byte)
        
        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            number = 0
        else:
            number = int(voltage / self.dynamic_range * 4095)
        
        self.set_number(number)
        
        if self.verbose:
            print(f"Установлено напряжение: {voltage:.2f} В -> число: {number}")


amplitude = float(input("Введите амплитуду сигнала (0-5.0 В): "))
signal_frequency = float(input("Введите частоту сигнала (Гц): "))
sampling_frequency = float(input("Введите частоту дискретизации (Гц): "))

dac = None

def get_triangle_wave_amplitude(frequency, time_point):
    period = 1 / frequency
    half_period = period / 2
    position = time_point % period
    
    if position < half_period:
        return 2 * position * frequency
    else:
        return 2 * (1 - position * frequency)

try:
    dac = MCP4725(5.0, 0x61, False)
    
    start_time = time.time()
    
    while True:
        current_time = time.time() - start_time
        normalized_amplitude = get_triangle_wave_amplitude(signal_frequency, current_time)
        voltage = normalized_amplitude * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    pass

finally:
    if dac:
        dac.deinit()