import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
red_led = 26
GPIO.setup(red_led, GPIO.OUT)
for i in range(0,6):
    if i%2==0:
        GPIO.output(red_led, GPIO.HIGH)
    else:
        GPIO.output(red_led, GPIO.LOW)
    print(i,"+--")
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
    time.sleep(0.5)
    print(i,"-+-")
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(22,GPIO.LOW)
    time.sleep(0.5)
    print(i,"--+")
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.HIGH)
    time.sleep(0.5)
GPIO.output(22,GPIO.LOW)