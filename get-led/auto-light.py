import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 26
GPIO.setup(LED_PIN, GPIO.OUT)

PHOTO_PIN = 6
GPIO.setup(PHOTO_PIN, GPIO.IN)

try:
    while True:
        GPIO.output(LED_PIN, not GPIO.input(PHOTO_PIN))
        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()