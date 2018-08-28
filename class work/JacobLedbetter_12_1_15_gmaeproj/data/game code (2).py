#Bunny Slipper Crusade
#jacob ledbetter and adam drouin
#9/29/13
#--------------------Notes-------------------------
# amazeing game
#--------------------------------------------------
#menu
import time

############## Import Libraries #######################
import pygame
import random
def go_thing():
    x=1
go_thing()
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
#sound load
music = pygame.mixer.Sound("./music.wav")
pew=pygame.mixer.Sound('./pew.wav')
enemy_dead=pygame.mixer.Sound('./enemy dead.wav')
jump=pygame.mixer.Sound('./jump.wav')
kitty_dead=pygame.mixer.Sound('./kitty_dead.wav')
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
test_2Img_l = pygame.image.load('kittyspringfinal.png')
test_2Img_r = pygame.image.load('kittyspringfinal.png')
test_3Img_l=pygame.image.load('melonlegs_l.png')
test_3Img_r=pygame.image.load('melonlegs_r.png')
projImg=pygame.image.load('./mellonleg_proj.png')
#play music
music.play(-1)
#player vars
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

test_2_x_chng=3
test_2_img=test_2Img_r
test_2_x_0=60
test_2_x_1=150
jump_timer=100
jump_timer_chng=-1
jumping_timer=60
test_2_y_0=650
s_wait=0

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
#lvl vars
checkpoint=0
lvl_comp=0
lvl_two_start=False
wait=0
inst=True
lvl_three_start=False
#game objects

#levels
def lvl_one():
    global wait,test1_x_0,test1_x_0_chng,test1_0_img,alien_0_dead,lvl_comp,player_img,player_x,player_y,player_y_change,player_x_change,player_x,player_proj_wall_colide,player_jumping,player_jump_height,player_jumptime,player_nohit_time,player_hit,hit,life,player_img,player_proj_chng,player_proj_x,player_proj_y,player_proj_wall_colide,player_proj_img,player_proj_fireing,player_proj_chng_chng,player_proj_dset,checkpoint
    def player(x,y):
        global player_img,player_x,player_y,player_y_change,player_x_change,player_x,player_proj_wall_colide,player_jumping,player_jump_height,player_jumptime,player_nohit_time,player_hit,hit,life,test1_x_0,test1_y_0,lvl_comp
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
        if player_y<=500:
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
                    time.sleep(1)
                    #player vars
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

                    test_2_x_chng=3
                    test_2_img=test_2Img_r
                    test_2_x_0=60
                    test_2_x_1=150
                    jump_timer=100
                    jump_timer_chng=-1
                    jumping_timer=60
                    test_2_y_0=650
                    #lvl vars
                    lvl_comp=0
                    checkpoint=0
                    
             
        player_x += player_x_change
        display.blit(player_img,(x,y))
    player(player_x,player_y)
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
                    enemy_dead.play()
                    alien_0_dead=True
                    player_proj_wall_colide=True
            test1_x_0+=test1_x_0_chng
            display.blit(test1_0_img,(x,y))
        testguy1_0(test1_x_0,test1_y_0)
    if alien_0_dead==True:
        lvl_comp+=1
        alien_0_dead=False

        test1_x_0=random.randint(10,705)
    if lvl_comp>=20:
        def win_text():
            font = pygame.font.SysFont("Calibri",32, False, False)
            text= font.render('Level Complete',True,black)
            display.blit(text,(250,400))
        win_text()
        wait+=1
        if wait>=20:
            wait=0
            time.sleep(2)
            checkpoint=1
        
def lvl_two():
    global wait,test_2_x_chng,test_2_img,test_2_x_0,test_2_x_1,jump_timer,jump_timer_chng,jumping_timer,test_2_y_0,alien_0_dead,lvl_comp,player_img,player_x,player_y,player_y_change,player_x_change,player_x,player_proj_wall_colide,player_jumping,player_jump_height,player_jumptime,player_nohit_time,player_hit,hit,life,player_img,player_proj_chng,player_proj_x,player_proj_y,player_proj_wall_colide,player_proj_img,player_proj_fireing,player_proj_chng_chng,player_proj_dset,lvl_two_start
    if lvl_two_start==False:
        lvl_comp=0
        lvl_two_start=True
    def player(x,y):
        global player_img,player_x,player_y,player_y_change,player_x_change,player_x,player_proj_wall_colide,player_jumping,player_jump_height,player_jumptime,player_nohit_time,player_hit,hit,life,test_2_x_0,test_2_y_0,lvl_comp
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
        if player_y<=500:
            player_jumping=False
            player_jump_hieght=0
            player_y=650
            player_jumptime=60
            
        if player_x+35  >= test_2_x_0 and player_x  <= test_2_x_0+35:
                if player_y+50 >= test_2_y_0 and player_y<= test_2_y_0+60:
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
                    time.sleep(1)
                    #player vars
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

                    test_2_x_0_chng=3
                    test_2_x_0=330
                    test_2_y_0=640
                    jump_timer=100
                    jump_timer_chng=-1
                    jumping_timer=60
                    test_2_y_0=650
                    #lvl vars
                    lvl_comp=0
                    checkpoint=1
        player_x += player_x_change
        display.blit(player_img,(x,y))
    player(player_x,player_y)
    if  alien_0_dead==False:
        #enemy in level
        def testguy_2(x,y):
            global s_wait,test_2_img,test_2_x_0,test_2_x_chng,jump_timer,jump_timer_chng,jumping_timer,test_2_y_0,player_proj_x,player_proj_y,alien_0_dead,player_proj_wall_colide
            if jump_timer==0:
                s_wait+=1
                if s_wait>=0:
                    jump.play()
                    s_wait=-120
                jump_timer_chng=0
                jumping_timer-=1
                test_2_y_0-=2
            if jumping_timer==0:
                test_2_y_0=650
                b_sound=False
                jump_timer=200
                jump_timer_chng=-1
                jumping_timer=120
            if test_2_x_0 >= 773:
                test_2_x_chng=-3
                test_2_img=test_2Img_l
            if test_2_x_0<=0:
                test_2_x_chng=3
                test_2_img=test_2Img_r
            if player_proj_x >= test_2_x_0 and player_proj_x+20 <= test_2_x_0+31:
                if player_proj_y >= test_2_y_0  and player_proj_y+20 <= test_2_y_0+60:
                    kitty_dead.play()
                    alien_0_dead=True
                    player_proj_wall_colide=True
            test_2_x_0+=test_2_x_chng
            jump_timer+=jump_timer_chng
            display.blit(test_2_img,(x,y))
        testguy_2(test_2_x_0,test_2_y_0)
    if alien_0_dead==True:
        lvl_comp+=1
        alien_0_dead=False

        test_2_x_0=random.randint(10,705)
    if lvl_comp>=20:

        def win_text():
            font = pygame.font.SysFont("Calibri",32, False, False)
            text= font.render('Level Complete',True,black)
            display.blit(text,(250,400))
        win_text()
        checkpoint=2
        wait+=1
        if wait>=20:
            wait=0
            time.sleep(2)
def lvl_three():
    global wait,test_3_img,test_3_x_chng,test_3_x_0,shoot_timer,proj_x,projtest_x,projtest_x_chng,wall,timer,timer_chng,alien_0_dead,lvl_comp,player_img,player_x,player_y,player_y_change,player_x_change,player_x,player_proj_wall_colide,player_jumping,player_jump_height,player_jumptime,player_nohit_time,player_hit,hit,life,player_img,player_proj_chng,player_proj_x,player_proj_y,player_proj_wall_colide,player_proj_img,player_proj_fireing,player_proj_chng_chng,player_proj_dset,lvl_three_start
    if lvl_three_start==False:
        lvl_comp=0
        lvl_three_start=True
    def player(x,y):
        global player_img,player_x,player_y,player_y_change,player_x_change,player_x,player_proj_wall_colide,player_jumping,player_jump_height,player_jumptime,player_nohit_time,player_hit,hit,life,test_2_x_0,test_2_y_0,lvl_comp
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
        if player_y<=500:
            player_jumping=False
            player_jump_hieght=0
            player_y=650
            player_jumptime=60
            
        if player_x+35  >= test_3_x_0 and player_x  <= test_3_x_0+35:
                if player_y+50 >= 645 and player_y<= 705:
                    if not player_hit:                
                        life-=1
                        player_hit=True
                        player_nohit_time=50
        if player_x+35  >= projtest_x and player_x  <= projtest_x+10:
                if player_y+50 >= 645 and player_y<= 665:
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
                    time.sleep(1)
                    #player vars
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

                    test_2_x_0_chng=3
                    test_2_x_0=330
                    test_2_y_0=640
                    jump_timer=100
                    jump_timer_chng=-1
                    jumping_timer=60
                    test_2_y_0=650

                    test_3_img=test_3Img_r
                    test_3_x_chng
                    test_3_x_0
                    shoot_timer
                    proj_x
                    projtest_x
                    projtest_x_chng
                    wall=True
                    timer
                    timer_chng
                    #lvl vars
                    lvl_comp=0
                    checkpoint=1
        player_x += player_x_change
        display.blit(player_img,(x,y))
    player(player_x,player_y)
    if  alien_0_dead==False:
        #enemy in level
        def testguy_3(x,y):
            global test_3_x_0,test_3_x_chng,test_3_img,timer,alien_0_dead
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
            if player_proj_x >= test_3_x_0 and player_proj_x+20 <= test_3_x_0+31:
                if player_proj_y >= 645  and player_proj_y+20 <= 705:
                    enemy_dead.play()
                    alien_0_dead=True
                    player_proj_wall_colide=True
            test_3_x_0+=test_3_x_chng
            display.blit(test_3_img,(x,y))
        testguy_3(test_3_x_0,645)

        if alien_0_dead==True:
                lvl_comp+=1
                alien_0_dead=False

                test_3_x_0=random.randint(10,705)
    if lvl_comp>=20:
        def win_text():
            font = pygame.font.SysFont("Calibri",32, False, False)
            text= font.render('Level Complete',True,black)
            display.blit(text,(250,400))
        win_text()
        checkpoint=3
        wait+=1
        if wait>=20:
            wait=0
            time.sleep(2)
            pygame.quit()
            quit()
       
#life count
def life_count(life):
    font = pygame.font.SysFont("Calibri",32, False, False)
    text= font.render(str(life),True,black)
    display.blit(lifecount,(0,0))
    display.blit(text,(20,10))
def enemy_count(comp):
    compdisp=str(comp)+'/20'
    font = pygame.font.SysFont("Calibri",32, False, False)
    text= font.render(compdisp,True,black)
    display.blit(text,(720,30))
def instructions():
    font = pygame.font.SysFont("Calibri",16, False, False)
    text= font.render('''arrows=movement and jump z=fire sumner head''',True,white)
    display.blit(text,(200,400))
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
                pew.play()
            if event.key==pygame.K_UP:
                player_jumping=True
                jump.play()
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
    if inst:
        wait+=1
        instructions()
        if wait>=20:
            time.sleep(7)
            inst=False
    if checkpoint==0:
        lvl_one()
    if checkpoint==1:
        lvl_two()
    if checkpoint==2:
        lvl_three()
        
        
    
    
   
########## Update screen and clock #############
#update the screen with the new drawing
    pygame.display.flip()
#set the clock speed
    clock.tick(24)
pygame.quit()
quit()






