import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 5, 25, 17, 27, 23, 22, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

up = 10
down = 9

GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

num = 0

def dec2bin(value):
    return [1 - int(element) for element in bin(value)[2:].zfill(8)]

sleep_time = 0.2

try:
    while True:
        up_pressed = GPIO.input(up)
        down_pressed = GPIO.input(down)
        
        if up_pressed and down_pressed:
            num = 255
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        elif up_pressed:
            num = num + 1
            if num > 255:
                num = 0
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        elif down_pressed:
            num = num - 1
            if num < 0:
                num = 255
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        
        GPIO.output(leds, dec2bin(num))
except KeyboardInterrupt:
    GPIO.cleanup()