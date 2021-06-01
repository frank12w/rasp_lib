import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.output([17, 27, 22, 26], GPIO.HIGH)
time.sleep(1)
GPIO.output([17, 27, 22, 26], GPIO.LOW)
for i in range(0,20):
    r = random.random()
    if r<0.3:
        led = 17
    elif r<0.6:
        led = 27
    elif r<0.9:
        led = 22
    else:
        led = 26
    print(led)
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(led, GPIO.LOW)
for i in range(5):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.1)
#GPIO.output([17, 27, 22, 26], GPIO.LOW)