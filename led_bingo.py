import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(26, GPIO.OUT) #red light
GPIO.setup(16, GPIO.OUT) #buzzer

GPIO.output(16, GPIO.HIGH)
GPIO.output([17, 27, 22, 26], GPIO.HIGH)
time.sleep(0.33)
GPIO.output(16, GPIO.LOW)
time.sleep(0.33)
GPIO.output(16, GPIO.HIGH)
time.sleep(0.33)
GPIO.output(16, GPIO.LOW)
GPIO.output([17, 27, 22, 26], GPIO.LOW)
print('*****START*****')
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
    #print(led)
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(led, GPIO.LOW)

#outcome 
if led==26: #red=bingo
    print('B!I!N!G!P!O!')
    for i in range(3):
        GPIO.output(led, GPIO.LOW)
        for j in range(10):
            GPIO.output(16, GPIO.HIGH)
            time.sleep(0.015)
            GPIO.output(16, GPIO.LOW)
            time.sleep(0.015)
        GPIO.output(led, GPIO.HIGH)
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
else:
    print('YOU LOSER')
#    GPIO.output(16, GPIO.HIGH)
    for i in range(3):
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led, GPIO.LOW)
        time.sleep(0.1) 
GPIO.output([17, 27, 22, 26, 16], GPIO.LOW)