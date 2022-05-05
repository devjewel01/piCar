from picamera import PiCamera
from time import sleep

camera = PiCamera()



camera.start_preview(alpha=200)
camera.annotate_text = "Car Camera"

camera.capture('/home/ict/car/camera/image/car.jpg')
    
camera.stop_preview()

