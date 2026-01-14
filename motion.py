import RPi.GPIO as GPIO
import time

PIR_PIN = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN)
    time.sleep(2)  # sensor warm-up

def motion_detected():
    return GPIO.input(PIR_PIN) == GPIO.HIGH

def cleanup():
    GPIO.cleanup()
