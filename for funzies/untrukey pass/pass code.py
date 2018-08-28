"""turkey pass
by adam drouin and jacob ledbetter

p1:
wasd=move
e=throw

p2: arows = move
r ctrl=throw

pass the turkey back and fourth"""

#import
import time
import pygame
#init
pygame.init()
#700x700
display_width=400
display_height=400
#color def
black=(0,0,0)
white=(255,255,255)
#surface prop
gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Turkey pass')
#clock
clock=pygame.time.Clock()
#pics
Turk1Img=pygame.image.load('./turk1.jpg')
Turk2Img=pygame.image.load('./turk2.jpg')
BallImg=pygame.image.load('./ball.jpg')
#spritwe loading
def turk1(x,y):
    gameDisplay.blit(Turk1Img,(x,y))
def turk2(x,y):
    gameDisplay.blit(Turk2Img,(x,y))
def ball(x,y):
    gameDisplay.blit(BallImg,(x,y))

#inital variables
t1_x=50
t1_y=200
t2_x=350
t2_y=200
t1_x_chng=0
t1_y_chng=0
t2_x_chng=0
t2_y_chng=0
b_x=t1_x
b_y=t1_y
b_ext=False
b_chng=1
fail=False
b_owner=1
score=0
#game loop
while not fail:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fail=True
    #fill white
    gameDisplay.fill(white)
    #p1 movement
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
                t2_x_chng= -5
        elif event.key==pygame.K_RIGHT:
                t2_x_chng=5
        elif event.key==pygame.K_UP:
                t2_y_chng= -5
        elif event.key==pygame.K_DOWN:
                t2_y_chng= 5
        elif event.key==pygame.K_RCTRL:
                    if b_owner==2:
                       b_ext=True
                    elif b_owner==1:
                        b_ext=False
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_RIGHT or event.key == pygame.K_LEFT:
                t2_x_chng=0
        elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                t2_y_chng=0
        elif event.key==pygame.K_RCTRL:
            if b_ext:
                    b_ext=True
            else:
                    b_ext=False
    t2_x += t2_x_chng
    t2_y += t2_y_chng

    #p2 movement
    if event.type == pygame.KEYDOWN:
        if event.key==pygame.K_a:
                t1_x_chng= -5
        elif event.key==pygame.K_d:
                t1_x_chng=5
        elif event.key==pygame.K_w:
                t1_y_chng= -5
        elif event.key==pygame.K_s:
                t1_y_chng= 5
        elif event.key==pygame.K_e:
            if b_owner==1:
                b_ext=True
            elif b_owner==2:
                b_ext=False
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_d or event.key == pygame.K_a:
                t1_x_chng=0
        elif event.key==pygame.K_w or event.key==pygame.K_s:
                t1_y_chng=0
        elif event.key==pygame.K_e:
            if b_ext:
                    b_ext=True
            else:
                b_ext=False
                
    t1_x += t1_x_chng
    t1_y += t1_y_chng

    #p2 ball movement
    if b_owner==1:

        
        b_y=t1_y+40
        if b_ext:
            if b_x < 400:
                b_x+=b_chng
                ball(b_x,b_y)
            else:
                
                fail=True
                b_ext=False
     #p1 ball movement
                if b_owner==2:
                    b_y=t2_y-40
                    
                    if b_ext:
                        if b2_x > 0:
                            b_x-=b_chng
                            ball(b_x,b_y)
                        else:
                            fail=True
                            b_ext=False
 #p1 ball to p2 colsion
    if b_x >= t2_x and b_x <= t2_x+51:
        if b_y >= t2_y and b_y<=t2_y+66:
            score+=1
            print(score)
            b_owner=2
            b_x=t2_x
            b_ext=False
    #p2 bullet to p1 colsion
    if b_x >= t1_x and b_x <= t1_x+51:
        if b_y >= t1_y and b_y<=t1_y+50:
            score+=1
            b_owner=1
            b_x=t1_x
            b_ext=False
     #sprite display
    turk1(t1_x,t1_y)
    turk2(t2_x,t2_y)
    #update
    pygame.display.update()
    #clock speed
    clock.tick(30)
#game end
pygame.quit()
quit()      
