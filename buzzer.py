import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)

dt1 = 1
dt2 = 2
for i in range(5):
    for j in range(10):
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.015)
        GPIO.output(16, GPIO.LOW)
        time.sleep(0.015)
    for j in range(10):
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.002)
        GPIO.output(16, GPIO.LOW)
        time.sleep(0.002)
    for j in range(3):
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.100)
        GPIO.output(16, GPIO.LOW)
        time.sleep(0.100)
    
    