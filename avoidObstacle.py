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
        sleep(1)
        Backward(20)
        sleep(1)
        Stop()
        sleep(0.5)

        ultraSonicLeft()
        sleep(1)
        L = Distance()
        print('Left Distance  is', L, 'm')
        sleep(0.5)
        ultraSonicPosition()
        sleep(0.5)

        ultraSonicRight()
        sleep(1)
        R = Distance()
        print('Right Distance  is', R, 'm')
        sleep(0.5)
        ultraSonicPosition()
        sleep(0.5)

        if L > R:
            Left(50)
            sleep(1)
            Stop()
            sleep(0.5)

        else:
            Right(50)
            sleep(1)
            Stop()
            sleep(0.5)
        
    else:
        Forward(20)

