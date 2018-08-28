

#Drawing and Movement with Sound
#Gavriel Feuer
#9/17/13
#--------------------Notes-------------------------
# -make sure the sound file is in the same folder as the bounce_player_sound.py file
#--------------------------------------------------
import pygame
#Define color palette
# r g b
BLACK = ( 0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = ( 0,255, 0)
BLUE = ( 0, 0,255)
#Initialize the pygame library
pygame.init()
#Set the size of the display canvas: Q-What are the units for the size?
size_x = 700
size_y = 500
size = [size_x, size_y]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Retro Screensaver")
# Sounds
# new sound
bounce_sound = pygame.mixer.Sound("./flyby.wav")

#Set the clock to manage how fast the screen updates
clock=pygame.time.Clock()
#Set up the shape parameters
radius = 50
line_width = 3
#set the starting position of our shape
position_x = 100
position_y = 100
#set the speed and direction of the shape
speed_x = 3
speed_y = 3

#This is the driving force for the program
rungame=True
#------------Main Program Loop -----------------
while rungame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame=False
#set the background color: Q- what would happen if this line was not included?
    screen.fill(WHITE)
#Draw the shape: Learn to look at the reference manual. DIY
#http://www.pygame.org/docs/ref/draw.html
# Outer circle
    pygame.draw.circle(screen, GREEN, [position_x, 10+position_y], radius, line_width)
# Head
    pygame.draw.circle(screen, BLACK, [1+position_x, -10+position_y], 10, 0 )
# Body
    pygame.draw.line(screen,RED,[position_x,25+position_y],[position_x,position_y],10)
# Arms
    pygame.draw.line(screen,RED,[position_x,8+position_y],[-20+position_x, 10+position_y],4)
    pygame.draw.line(screen,RED,[position_x,8+position_y],[ 20+position_x, 10+position_y],4)
# Legs
    pygame.draw.line(screen,BLUE,[position_x-2,25+position_y],[-8+position_x,45+position_y],6)
    pygame.draw.line(screen,BLUE,[position_x+2,25+position_y],[ 8+position_x,45+position_y],6)
#Move the shape
    position_x = position_x + speed_x
    position_y = position_y + speed_y
#Bounce the ball if it hits a wall or an obstacle
    if position_x > size_x-radius or position_x < 0+radius:
        speed_x = -1*speed_x
        bounce_sound.play()

    if position_y > size_y-radius or position_y < 0+radius:
        speed_y = -1*speed_y
        bounce_sound.play()
#Set the clock speed [frames per second]
    clock.tick(60)
#Update the screen with the new drawing
    pygame.display.flip()
pygame.quit()
