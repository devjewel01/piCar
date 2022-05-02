from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180


camera.start_preview(alpha=200)
camera.annotate_text = "Car Camera"
for i in range(5):
    sleep(3)
    camera.capture('/home/ict/car/camera/image/img%s.jpg' % i)
    
camera.stop_preview()

