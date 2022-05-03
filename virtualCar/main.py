

from motor import Forward, Backward, Right, Left, Stop
import pygame
from time import sleep


# initialize things
pygame.init()
robot = serial.Serial(PORT, BUADRATE)  


window = pygame.display.set_mode((700,400))  
#window = pygame.display.set_mode((1155,399))   


bg  = pygame.image.load("image/track1.png")
#bg  = pygame.image.load("image/track2.png")
car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (40, 40)) 


clock = pygame.time.Clock()


car_x = 30   
car_y = 260  

JUMP_VALUE = 25     # turning point value
direction = 'y_up'  # cars current direction
run = 1


Forward()
DELAY = .400
# main loop
while run:
    clock.tick(30)        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    # position images
    window.blit(bg, (0, 0))          # load the track image
    window.blit(car, (car_x, car_y)) # the car image


    last_x, last_y = car_x, car_y
    
    # find the center of the car and draw a point on that
    center_x, center_y = (int(car_x + 40 /2), int(car_y + 40 / 2))
    pygame.draw.circle(window, (0,255,255), (center_x, center_y), 5, 5)

   
    cal_value = 30             
    y_up      = window.get_at((center_x, center_y - cal_value))[0]
    y_down    = window.get_at((center_x, center_y + cal_value))[0]
    x_right   = window.get_at((center_x + cal_value, center_y))[0]
    x_left    = window.get_at((center_x - cal_value, center_y))[0]
    #print("y_up   ", y_up)
    #print("y_down ", y_down)
    #print("x_right", x_right)
    #print("x_left ", x_left)
    #print("-----------")

    # determine which way to go
    # go up
    if y_up == 255 and direction == 'y_up' and x_left != 255 and x_right != 255:
        # move up
        car_y -= 2  # decrease pixel and move the car on y axis
        
    # make the turn
    if y_up == 255 and direction == 'y_up' and x_left != 255 and x_right == 255:
        # make a right turn
        direction = 'x_right'
        car_y -= JUMP_VALUE
        car_x += JUMP_VALUE
        car = pygame.transform.rotate(car, -90)
        window.blit(car, (car_x, car_y))
        print('Turn Right')
        Right()
        sleep(DELAY)
        Forward()

    # go x right
    if y_up != 255 and direction == 'x_right' and y_down != 255 and x_right == 255:
        car_x += 2

    if y_down == 255 and direction == 'x_right' and x_left == 255 and x_right == 255:
        # make a turn from x_right
        car = pygame.transform.rotate(car, -90)
        direction = 'y_down'
        car_y += JUMP_VALUE + 5
        car_x += JUMP_VALUE
        window.blit(car, (car_x, car_y))
        print('Turn Right')
        Right()
        sleep(DELAY)
        Forward()

    # go y down
    if y_down == 255 and direction == 'y_down' and x_left != 255 and x_right != 255:
        # move down
        car_y += 2

    # left turn
    if y_down == 255 and direction == 'y_down' and x_left != 255 and x_right == 255:
        # turn from y_down
        car = pygame.transform.rotate(car, 90)
        direction = 'x_right'
        car_y += JUMP_VALUE
        car_x += JUMP_VALUE
        print('Turn left')
        Left()
        sleep(DELAY)
        Forward()
    
    # turn to y up
    if y_up == 255 and direction == 'x_right' and x_left == 255 and x_right == 255:
        # turn from y_down
        car = pygame.transform.rotate(car, 90)
        direction = 'y_up'
        car_y -= JUMP_VALUE + 5
        car_x += JUMP_VALUE
        print('Turn left')
        Left()
        sleep(DELAY)
        Forward()
    
    # if car is stopped
    if car_x == last_x and car_y == last_y:
        # stop the engine sound
        print("STOPPED")
        Stop()
        
    pygame.display.update()  # update the window

pygame.quit()      #close everything