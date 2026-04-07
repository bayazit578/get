import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 26
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 200)
duty = 0.0
pwm.start(duty)

try:
    while True:
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.05)
        
        duty += 1.0
        if duty > 100.0:
            duty = 0.0
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()