from picamera import PiCamera
from time import sleep

camera = PiCamera()

 #   camera.start_preview()
 #   sleep(2)
 #   camera.stop_preview()

 #   camera.resolution = (480, 480)
 #   camera.start_preview()
 #   sleep(2)
 #   camera.stop_preview()

camera.preview_fullscreen = False
camera.preview_window = (0, 0, 480, 480)
camera.start_preview()
camera.start_recording('/home/pi/usbcamera_test/picam2.h264') #video
camera.capture('/home/pi/usbcamera_test/picam2.jpg') #picture
sleep(60)
#camera.start_preview(fullscreen=False, window = (0, 0, 480, 480))
camera.preview_window = (0, 0, 640, 1000)
sleep(2)
camera.stop_preview()
camera.stop_recording()