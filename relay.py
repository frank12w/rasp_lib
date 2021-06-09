import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)
time.sleep(0.2) #need more than 0.1sec
GPIO.output(2,GPIO.LOW)
time.sleep(1)