



#Bunny Slipper Crusade
#jacob ledbetter and adam drouin
#9/29/13
#--------------------Notes-------------------------
# amazeing game
#--------------------------------------------------
############## Import Libraries #######################
import pygame
import random
import time
############## Define Variables/Initilization #######################
#All variable definitions, functions, and class objects go below this line
pygame.init()


iconImg=pygame.image.load('./icon.png')
pygame.display.set_icon(iconImg)

#Define color palette
# r g b
black = ( 0, 0, 0)
white = (255,255,255)
red = (255, 0, 0)
green = ( 0,255, 0)
blue = ( 0, 0,255)
#set display parameters
size_x=800
size_y=700
size=[size_x,size_y]
class requirement:
    xyz=0

display=pygame.display.set_mode(size)
pygame.display.set_caption("Bunny slipper crusade")
#image loading
test_1Img_l = pygame.image.load('enemeesprite_l.png')
test_1Img_r = pygame.image.load('./enemeesprite_r.png')
test_2Img_l = pygame.image.load('kittyspringfinal.png')
test_2Img_r = pygame.image.load('kittyspringfinal.png')
test_3Img_l=pygame.image.load('melonlegs_l.png')
test_3Img_r=pygame.image.load('melonlegs_r.png')
projImg=pygame.image.load('./mellonleg_proj.png')
#game vars
jump_add=1
life=2
test_1_x_chng=3
test_1_img=test_1Img_r
test_1_x_0=30
test_1_x_1=120
test_2_x_chng=3
test_2_img=test_2Img_r
test_2_x_0=60
test_2_x_1=150
jump_timer=100
jump_timer_chng=-1
jumping_timer=60
test_2_y=650
test_3_img=test_3Img_r
test_3_x_chng=3
test_3_x_0=200
shoot_timer=3
proj_x=test_3_x_0
projtest_x=200
projtest_x_chng=3
wall=True
timer=2
timer_chng=1
#game objects
def testguy_1(x,y):
    global test_1_x_0,test_1_x_chng,test_1_img
    if test_1_x_0 >= 773:
        test_1_x_chng=-3
        test_1_img=test_1Img_l
    if test_1_x_0<=0:
        test_1_x_chng=3
        test_1_img=test_1Img_r
    test_1_x_0+=test_1_x_chng
    display.blit(test_1_img,(x,y))
def testguy_2(x,y):
    global test_2_img,test_2_x_0,test_2_x_chng,jump_timer,jump_timer_chng,jumping_timer,test_2_y
    if jump_timer==0:
        jump_timer_chng=0
        jumping_timer+=-1
        test_2_y-=2
        if jumping_timer==0:
            test_2_y=650
            jump_timer=200
            jump_timer_chng=-1
            jumping_timer=120
    if test_2_x_0 >= 773:
        test_2_x_chng=-3
        test_2_img=test_2Img_l
    if test_1_x_0<=0:
        test_2_x_chng=3
        test_2_img=test_2Img_r
    test_2_x_0+=test_2_x_chng
    jump_timer+=jump_timer_chng


    
    display.blit(test_2_img,(x,y))
def testguy_3(x,y):
    global test_3_x_0,test_3_x_chng,test_3_img,timer
    


    def projtest(y):
        global projtest_x,projtest_x_chng,est_2_x_0,wall,timer,timer_chng,test_3_img
        if test_3_img==test_3Img_l:
            projtest_chng_chng=5
        if test_3_img==test_3Img_r:
            projtest_chng_chng=-5
        if projtest_x<=0:
            timer_chng=0
            projtest_x=test_3_x_0
            projtest_x_chng=0
            wall=True
            timer=120
            timer_chng=1
        if projtest_x>=777:
            timer_chng=0
            projtest_x=test_3_x_0
            projtest_x_chng=0
            wall=True
            timer=120
            timer_chng=1
        if wall:
            projtest_x=test_3_x_0
            timer-=timer_chng
        if timer==0:
           timer=120
           wall=False
           projtest_x_chng=projtest_chng_chng
        projtest_x-=projtest_x_chng
        display.blit(projImg,(projtest_x,y))
    projtest(655)
    if test_3_x_0 >= 773:
        test_3_x_chng=-3
        test_3_img=test_3Img_l
    if test_3_x_0<=0:
        test_3_x_chng=3
        test_3_img=test_3Img_r
    test_3_x_0+=test_3_x_chng
    display.blit(test_3_img,(x,y))





#set the clock to manage how fast the screen updates
clock=pygame.time.Clock()
#Setup the loop control
rungame=True
#------------Main Program Loop -----------------
while rungame:
########## Events ######################
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               rungame=False
     display.fill(white)
     
######### Begin Game Logic ####################
#Start by clearing the old display
     
######### End Game Logic ######################

     testguy_1(test_1_x_0,640)
     #testguy_1(test_1_x_1,640)
     testguy_2(test_2_x_0,test_2_y)
     #testguy_2(test_2_x_1,test_2_y)
     testguy_3(test_3_x_0,645)
########## Update screen and clock #############
#update the screen with the new drawing
     pygame.display.flip()
#set the clock speed
     clock.tick(30)   
pygame.QUIT
quit()




