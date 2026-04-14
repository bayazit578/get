import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

button = 13

GPIO.setup(button, GPIO.IN)

state = 0

GPIO.output(led, state)

last_button_state = 0

try:
    while True:
        current_button_state = GPIO.input(button)

        if current_button_state and not last_button_state:
            state = not state
            GPIO.output(led, state)
            time.sleep(0.05)

        last_button_state = current_button_state
        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
