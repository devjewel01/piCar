from buzzer import Buzzer
from motor import Forward, Backward, Left, Right, Stop
from time import sleep
from ultraSonic import Distance
from servo import ultraSonicLeft, ultraSonicPosition, ultraSonicRight


while True: 
    d = Distance()
    print('Front Distance  is', d, 'cm')   
    if d < 10.0:
        Stop()
        Buzzer()  
        sleep(0.5)
        Backward(20)
        sleep(0.8)
        Stop()
        sleep(0.3)

        ultraSonicLeft()
        sleep(0.5)
        L = Distance()
        print('Left Distance  is', L, 'm')
        sleep(0.5)
        ultraSonicPosition()
        sleep(0.5)

        ultraSonicRight()
        sleep(0.5)
        R = Distance()
        print('Right Distance  is', R, 'm')
        sleep(0.5)
        ultraSonicPosition()
        sleep(0.5)

        if L > R:
            Left(60)
            sleep(0.3)
            Stop()
            sleep(0.5)

        else:
            Right(60)
            sleep(0.3)
            Stop()
            sleep(0.5)
        
    else:
        Forward(20)

