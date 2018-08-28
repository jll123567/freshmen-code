
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


display=pygame.display.set_mode(size)
pygame.display.set_caption("Bunny slipper crusade")
#image loading
player_r_Img = pygame.image.load('supersprite_r.png')
player_l_Img = pygame.image.load('supersprite_L.png')
player_j_r_Img=pygame.image.load('superspritejump_r.png')
player_j_l_Img=pygame.image.load('superspritejump_l.png')
player_proj_r_Img=pygame.image.load('sum_r.png')
player_proj_l_Img=pygame.image.load('sum_l.png')
#enemy img load
test_1Img_l = pygame.image.load('enemeesprite_l.png')
test_1Img_r = pygame.image.load('./enemeesprite_r.png')
#game vars
player_x=100
player_y=650
player_x_change=0
player_y_change=0
player_img=player_l_Img
player_proj_chng=0
player_proj_chng_chng=0
player_proj_x=player_x
player_proj_y=player_y
player_proj_wall_colide=True
player_proj_fireing=False
player_proj_dset=False
player_jump_height=0

player_y=650
player_jumptime=60
player_jumping=False
hit=0
player_nohit_time=60
player_hit=False
life=500
#enemy vars
test_1_x_chng=3
test_1_img=test_1Img_r
test_1_x_0=330
test_1_y_0=640
alien_1_dead=False
#enemy object
def testguy_1(x,y):
    global test_1_x_0,test_1_x_chng,test_1_img,alien_1_dead
    if test_1_x_0 >= 773:
        test_1_x_chng=-3
        test_1_img=test_1Img_l
    if test_1_x_0<=0:
        test_1_x_chng=3
        test_1_img=test_1Img_r
    if player_proj_x >= test_1_x_0 and player_proj_x+20 <= test_1_x_0+31:
        if player_proj_y >= test_1_y_0  and player_proj_y+20 <= test_1_y_0+60:
            alien_1_dead=True
            print('hit')
            
    test_1_x_0+=test_1_x_chng
    display.blit(test_1_img,(x,y))
#game objects
def player(x,y):
    global player_img,player_x,player_y,player_y_change,player_x_change,player_x,player_proj_wall_colide,player_jumping,player_jump_height,player_jumptime,player_nohit_time,player_hit,hit,life
    def proj():
        global player_img,player_proj_chng,player_proj_x,player_proj_y,player_proj_wall_colide,player_proj_img,player_proj_fireing,player_proj_chng_chng,player_proj_dset
        player_proj_y=player_y
        if not player_proj_dset:
            if player_img==player_r_Img or player_img==player_j_r_Img:
                if player_proj_chng_chng==0:
                    player_proj_chng_chng=0
                else:  
                    player_proj_chng_chng=5
                player_proj_img=player_proj_r_Img
        if not player_proj_dset:
            if player_img==player_l_Img or player_img==player_j_l_Img:
                player_proj_img=player_proj_l_Img
                if player_proj_chng_chng==0:
                    player_proj_chng_chng=0
                else:
                        player_proj_chng_chng=-5
        if player_proj_x<=0:
             player_proj_x=player_x
             player_proj_x_chng_chng=0
             player_proj_wall_colide=True
        if player_proj_x>=777:
            player_proj_x=player_x
            projtest_x_chng_chng=0
            player_proj_wall_colide=True
        if player_proj_wall_colide:
            player_proj_dset=False
            player_proj_x=player_x
            player_proj_chng_chng=0
        if player_proj_fireing:
            player_proj_wall_colide=False
            if player_img==player_r_Img or player_img==player_j_r_Img:
                player_proj_chng_chng=5
                player_proj_img=player_proj_r_Img
            if player_img==player_l_Img or player_img==player_j_l_Img:
                player_proj_img=player_proj_l_Img
                player_proj_chng_chng=-5
        player_proj_chng=player_proj_chng_chng
        player_proj_x+=player_proj_chng
        display.blit(player_proj_img,(player_proj_x,player_proj_y))
    proj()

    if player_jumping==True:
        player_jump_height=-2
        player_jumptime-=1
        player_y += player_jump_height
    if player_jumptime<=0:
        player_jumping=False
        player_y +=2
        player_y=650
        player_jumptime=60
    if player_y<=540:
        player_jumping=False
        player_jump_hieght=0
        player_y=650
        player_jumptime=60
    if player_x+35  >= test_1_x_0 and player_x  <= test_1_x_0+35:
            #print('xhit')
            if player_y+50 >= test_1_y_0 and player_y<= test_1_y_0+60:
                #print('yhit')

                if not player_hit:
                    #print('no inv')
       
            
                
                    life-=1
                    player_hit=True

                    player_nohit_time=50
                    #print('hit',life)
    if player_hit:
        #print('block',player_nohit_time)
        if player_nohit_time>0:
            player_nohit_time-=1
        else:
            player_hit=False
            player_nohit_time=50
    if life <= 0:
        print('ded')
        quit()


            
    player_x += player_x_change
    display.blit(player_img,(x,y))
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
    if hit>=1:
        hit=0
     
######### Begin Game Logic ####################
    if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_z:
                player_proj_fireing = True
                player_proj_dset=True
            if event.key==pygame.K_UP:
                player_jumping=True
            if event.key==pygame.K_x:
                hit+=2
                
            if event.key==pygame.K_LEFT:
                player_x_change= -4
                player_img=player_l_Img
            elif event.key==pygame.K_RIGHT:
                player_x_change=4
                player_img=player_r_Img
    if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                if player_jumping:
                    player_jumping=True
                else:
                    player_jumping=False
            if  event.key==pygame.K_z:
                player_proj_fireing=False
            if event.key==pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_x_change=0
            
     
######### End Game Logic ######################
    player(player_x,player_y)
    if alien_1_dead==False:
        testguy_1(test_1_x_0,test_1_y_0)

########## Update screen and clock #############
#update the screen with the new drawing
    pygame.display.flip()
#set the clock speed
    clock.tick(24)
pygame.quit
quit()





