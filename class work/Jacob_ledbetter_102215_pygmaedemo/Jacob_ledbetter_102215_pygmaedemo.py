#------------------------------------------





#press f5
#arows to move
#get hearts avoid green thing
#if you die try again
#good luck



#_______----------------------------
#import
import pygame
import random
import time
#init
pygame.init()
#surface size
display_width=1000
display_height=600
#color def
black= (0,0,0)
white=(255,255,255)
red=(255,0,0)
cyan=(65,255,243)
#more surface info
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('demo')
#clock
clock = pygame.time.Clock()
#the refrence imiges
faceImg = pygame.image.load('face.png')
hrtImg=pygame.image.load('hrt_sml.png')
badImg=pygame.image.load('bad.png')
#runing the  elements
def bad(x,y):
    gameDisplay.blit(badImg,(x,y))
def face(x,y):
    gameDisplay.blit(faceImg,(x,y))
def heart(x,y):
    gameDisplay.blit(hrtImg,(x,y))
    #dif
def dif():
    global hrt_count
    if hrt_count==10:
        bad(badx-100,bady+10)
def score(count):
    font = pygame.font.SysFont('./fontp',32)
    text= font.render(str(count),True,black)
    gameDisplay.blit(text,(0,0))
#start pos
facex=(display_width*0.68)
facey=(display_height*0.4)
hrtx=(display_width*0.34)
hrty=facey
badx=random.randint(20,950)
bady=random.randint(20,550)
#hrtcounter
hrt_count=0
#the change vars
facex_change=0
facey_change=0
badx_chng=5
bady_chng=5
#crash var(old)
crashed = False
#game loop
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            quit()
            
        #border fix
        if facex > display_width:
                facex -= 150
        elif facex < 0:
                facex += 150
        elif facey > display_height:
            facey -= 50
        elif facey < 0:
            facey += 50
        #movement
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                facex_change= -5
            elif event.key==pygame.K_RIGHT:
                facex_change=5
            elif event.key==pygame.K_UP:
                facey_change= -5
            elif event.key==pygame.K_DOWN:
                facey_change= 5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT or event.key == pygame.K_LEFT:
                facex_change=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                facey_change=0
    facex += facex_change
    facey += facey_change
    #dif change
    dif()
    #bad movement
    if bady > 580:
            bady_chng=bady_chng*-1
            bady_chng-=1
    elif bady < 20:
            bady_chng=bady_chng**1
            bady_chng+=1
    elif badx > 980:
            badx_chng=badx_chng*-1
            badx_chng-=1
            
    elif badx < 20:
            badx_chng=badx_chng**1
            badx_chng +=1
    badx +=badx_chng
    bady += bady_chng
    #hrt colection
    if facex >= hrtx - 50 and facex <= hrtx +50:
        if facey >= hrty-50 and facey<=hrty+50:
             hrt_count += 1
             hrtx=random.randint(0,950)
             hrty=random.randint(0,550)
    #bad colision detection
    if facex >= badx- 50 and facex <= badx +50:
        if facey >= bady-50 and facey<=bady+50:
            print('you ded')
            print('score:',hrt_count)
            time.sleep(2)
            pygame.quit()
            time.sleep(2
                       )
            quit()
        #background
    gameDisplay.fill(cyan)
    heart(hrtx,hrty)
    face(facex,facey)
    bad(badx,bady)
    score(hrt_count)
    
    #update
    pygame.display.update()
    clock.tick(30)
#quit
    
pygame.quit()
quit()
#complete!!!
