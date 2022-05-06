from motor import Forward, Stop
from ultraSonic import Distance

while True:
    if Distance() < 15:
        Forward(30)
    else:
        Stop()
