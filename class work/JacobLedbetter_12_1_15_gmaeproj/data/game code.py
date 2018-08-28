#Bunny Slipper Crusade
#jacob ledbetter and adam drouin
#9/29/13
#--------------------Notes-------------------------
# amazeing game
#--------------------------------------------------
#menu
import time
print('''press p to play
press c for credits
press q to quit''')
command=input()
if command == 'p':
    print('''playing...''')
if command=='c':
    print('''code by  jacob
everything else by adam''')
    time.sleep(5)
if command=='q':
    quit()
else:
    p=1

############## Import Libraries #######################
import pygame
import random
############## Define Variables/Initilization #######################
#All variable definitions, functions, and class objects go below this line
pygame.init()
#corner icon
iconImg=pygame.image.load('./icon.png')
pygame.display.set_icon(iconImg)
#Define color palette
# r g b
black = ( 0, 0, 0)
white = (255,255,255)
red = (255, 0, 0)
green = ( 0,255, 0)
blue = ( 0, 0,255)
grass_green=(15,219,20)
#set display parameters
size_x=800
size_y=700
size=[size_x,size_y]
#program name
display=pygame.display.set_mode(size)
pygame.display.set_caption("Bunny slipper crusade")    
#image loading
bground=pygame.image.load('bg.png')
lifecount=pygame.image.load('heart_new.png')

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
life=7
#enemy vars
test1_x_0_chng=3
test1_0_img=test_1Img_r
test1_x_0=330
test1_y_0=640
alien_0_dead=False
test1_x_1_chng=3
test1_1_img=test_1Img_r
test1_x_1=330
test1_y_1=640
alien_1_dead=False
test1_x_2chng=3
test1_2_img=test_1Img_r
test1_x_2=330
test1_y_2=640
alien_2_dead=False
#enemy object
lvl_comp=0
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
        player_jump_height=-3
        player_jumptime-=1
        player_y += player_jump_height
    if player_jumptime<=0:
        player_jumping=False
        player_y +=3
        player_y=650
        player_jumptime=60
    if player_y<=540:
        player_jumping=False
        player_jump_hieght=0
        player_y=650
        player_jumptime=60
        
    if player_x+35  >= test1_x_0 and player_x  <= test1_x_0+35:
            if player_y+50 >= test1_y_0 and player_y<= test1_y_0+60:
                if not player_hit:                
                    life-=1
                    player_hit=True
                    player_nohit_time=50
    if player_hit:
        if player_nohit_time>0:
            player_nohit_time-=1
        else:
            player_hit=False
            player_nohit_time=50
    if life <= 0:
         pygame.quit()
         print('game_over')
         time.sleep(7)
         quit()
         
    player_x += player_x_change
    display.blit(player_img,(x,y))
#levels
def lvl_one():
    global test1_x_0,test1_x_0_chng,test1_0_img,alien_0_dead,lvl_comp
    if  alien_0_dead==False:
        #enemy in level
        def testguy1_0(x,y):
            global test1_x_0,test1_x_0_chng,test1_0_img,alien_0_dead,player_proj_wall_colide
            if test1_x_0 >= 773:
                test1_x_0_chng=-3
                test1_0_img=test_1Img_l
            if test1_x_0<=0:
                test1_x_0_chng=3
                test1_0_img=test_1Img_r
            if player_proj_x >= test1_x_0 and player_proj_x+20 <= test1_x_0+31:
                if player_proj_y >= test1_y_0  and player_proj_y+20 <= test1_y_0+60:
                    alien_0_dead=True
                    player_proj_wall_colide=True
            test1_x_0+=test1_x_0_chng
            display.blit(test1_0_img,(x,y))
        testguy1_0(test1_x_0,test1_y_0)
    if alien_0_dead==True:
        lvl_comp+=1
        alien_0_dead=False

        test1_x_0=random.randint(10,705)
    if lvl_comp>=25:
        pygame.quit()
        print('YOU WIN!!!')
        time.sleep(7)
        quit()
#life count
def life_count(life):
    font = pygame.font.SysFont('./fontp',32)
    text= font.render(str(life),True,black)
    display.blit(lifecount,(0,0))
    display.blit(text,(20,10))
def enemy_count(comp):
    compdisp=str(comp)+'/25'
    font = pygame.font.SysFont('./fontp',32)
    text= font.render(compdisp,True,black)
    display.blit(text,(740,30))
        
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
               
    display.fill(grass_green)
    display.blit(bground,(0,0))
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
    life_count(life)
    enemy_count(lvl_comp)
    player(player_x,player_y)
    lvl_one()
        
    
    
   
########## Update screen and clock #############
#update the screen with the new drawing
    pygame.display.flip()
#set the clock speed
    clock.tick(24)
pygame.quit()
quit()






