import pygame
import time
#init
pygame.init()
#surface size
display_width=600
display_height=600
#color def
black= (0,0,0)
white=(255,255,255)
red=(255,0,0)
cyan=(65,255,243)
#more surface info
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('this is all you get')
#clock
clock = pygame.time.Clock()
#the refrence imiges
Card0= pygame.image.load('./c0.png')
Card1= pygame.image.load('./c1.png')
Card2= pygame.image.load('./c2.png')
Card3= pygame.image.load('./c3.png')
Card4= pygame.image.load('./c4.png')
#runing the  elements
def crd0(x,y):
    gameDisplay.blit(Card0,(x,y))
def crd1(x,y):
    gameDisplay.blit(Card1,(x,y))
def crd2(x,y):
    gameDisplay.blit(Card2,(x,y))
def crd3(x,y):
    gameDisplay.blit(Card3,(x,y))
def crd4(x,y):
    gameDisplay.blit(Card4,(x,y))
all_y=200
i = True
while i:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            i=False
        gameDisplay.fill(white)
        crd0(0,all_y)
        crd1(120,all_y)
        crd2(240,all_y)
        crd3(360,all_y)#360? 360 noscope!
        crd4(480,all_y)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
