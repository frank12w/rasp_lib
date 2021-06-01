from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
i = 3    
camera.start_recording('/home/pi/usbcamera_test/video%s.h264' %i) #video
camera.capture('/home/pi/usbcamera_test/picture%s.jpg' %i) #picture
sleep(60)
camera.stop_recording()
camera.stop_preview()
print(i)
