from buzzer import Buzzer
from ultraSonic import Distance

while True:
    if Distance() < 15:
        buzzer()

