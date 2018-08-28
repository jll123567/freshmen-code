"""-----------------------------
ctrl+f9 to start
p1:
    move=arow keys
    shoot=right ctrl
p2:
    move=wasd
    shoot=e
kill other player to win
----------------------------"""
#import
import time
import pygame
#init
pygame.init()
#700x700
display_width=700
display_height=700
#color def
black=(0,0,0)
white=(255,255,255)
#surface prop
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('chicken fighter')
#clock
clock=pygame.time.Clock()
#pics
chickenImg=pygame.image.load('./chicken_2.jpg')
chicken2Img=pygame.image.load('./chicken_1.jpg')
bulletImg=pygame.image.load('./bullet2.jpg')
bullet2Img=pygame.image.load('./bullet.jpg')
#spritwe loading
def chick1(x,y):
    gameDisplay.blit(chickenImg,(x,y))
def chick2(x,y):
    gameDisplay.blit(chicken2Img,(x,y))
def b1(x,y):
    gameDisplay.blit(bulletImg,(x,y))
def b2(x,y):
    gameDisplay.blit(bullet2Img,(x,y))
#inital variables
c1_x=525
c1_y=350
c2_x=175
c2_y=350
c1_x_chng=0
c1_y_chng=0
c2_x_chng=0
c2_y_chng=0
b1_x=c1_x
b1_y=c1_y
b2_x=c2_x+30
b2_y=c2_y
b1_chng=5
b1_ext=False
b2_ext=False
b2_chng=5
red_ded=False
blue_ded=False
tie=False
#game loop
while not red_ded or blue_ded or tie:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tie=True
    #fill white
    gameDisplay.fill(white)
    #p1 movement
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
                c1_x_chng= -5
        elif event.key==pygame.K_RIGHT:
                c1_x_chng=5
        elif event.key==pygame.K_UP:
                c1_y_chng= -5
        elif event.key==pygame.K_DOWN:
                c1_y_chng= 5
        elif event.key==pygame.K_RCTRL:
                   b1_ext=True
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_RIGHT or event.key == pygame.K_LEFT:
                c1_x_chng=0
        elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                c1_y_chng=0
        elif event.key==pygame.K_RCTRL:
            if b1_ext:
                    b1_ext=True
            else:
                    b1_ext=False
    c1_x += c1_x_chng
    c1_y += c1_y_chng

    #p2 movement
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_a:
                c2_x_chng= -5
        elif event.key==pygame.K_d:
                c2_x_chng=5
        elif event.key==pygame.K_w:
                c2_y_chng= -5
        elif event.key==pygame.K_s:
                c2_y_chng= 5
        elif event.key==pygame.K_e:
                b2_ext=True
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_d or event.key == pygame.K_a:
                c2_x_chng=0
        elif event.key==pygame.K_w or event.key==pygame.K_s:
                c2_y_chng=0
        elif event.key==pygame.K_e:
            if b2_ext:
                    b2_ext=True
            else:
                    b2_ext=False
    c2_x += c2_x_chng
    c2_y += c2_y_chng

    #p1 bullet movement
    b1_y=c1_y
    if b1_ext:
        if b1_x > 0:
                b1_x-=b1_chng
                b1(b1_x,b1_y)
        else:
                b1_ext=False
                b1_x=c1_x
    #p2 bullet movement
    b2_y=c2_y
    if b2_ext:
        if b2_x < 700:
                b2_x+=b2_chng
                b2(b2_x,b2_y)
        else:
                b2_ext=False
                b2_x=c2_x
    #p1 bullet to p2 colsion
    if b1_x >= c2_x and b1_x <= c2_x+72:
        if b1_y >= c2_y and b1_y<=c2_y+63:
            print('red wins')
            time.sleep(2)
            pygame.quit()
    #p2 bullet to p1 colsion
    if b2_x >= c1_x and b2_x <= c1_x +72:
        if b2_y >= c1_y and b2_y<=c1_y+63:
            print('blue wins')
            time.sleep(2)
            pygame.quit()


    #sprite display
    chick1(c1_x,c1_y)
    chick2(c2_x,c2_y)
    #update
    pygame.display.update()
    #clock speed
    clock.tick(30)
#game end(broken?)
pygame.QUIT()
quit()
#!!!COMPLETE!!!#
