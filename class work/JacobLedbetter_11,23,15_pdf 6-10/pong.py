#Pong
#Gavriel Feuer
#12/4/13
#--------------------Notes--------------------------------------------------------
#In computer graphics, a sprite is a two-dimensional image or animation that is
# integrated into a larger scene.
#--------Import Libraries-------------------------------------------------------
import pygame
#-------------Color Pallet------------------------
black = ( 0, 0, 0)
white = (255,255,255)
red = (255, 0, 0)
green = ( 0,255, 0)
blue = ( 0, 0,255)
#-------------Initializations-----------------------
pygame.init()
screensize_x=700
screensize_y=500
screensize=[screensize_x,screensize_y]
screen_color=black
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Pong")
font = pygame.font.Font(None, 36)
background = pygame.Surface(screen.get_size())
clock=pygame.time.Clock()
paddle_width=20
paddle_height=80
#--------------Player Sprite-------------------
class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.width=paddle_width
        self.height=paddle_height
        self.image=pygame.Surface([self.width,self.height])
        self.image.fill(white)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed_x=0
        self.speed_y=0
def move(self):
    self.rect.x+=self.speed_x
    self.rect.y+=self.speed_y
def collide(self):
    if self.rect.y<0:
        self.rect.y=0
    if self.rect.y>screensize_y-self.height:
        self.rect.y=screensize_y-self.height
    if self.rect.x<0:
        self.rect.x=0
    if self.rect.x>screensize_x-self.width:
        self.rect.x=screensize_x-self.width
#--------------Ball Sprite-------------------
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width=10
        self.height=10
        self.image=pygame.Surface([self.width,self.height])
        self.image.fill(blue)
        self.rect=self.image.get_rect()
        self.rect.x=screensize_x/2
        self.rect.y=screensize_y/2
        self.speed_x=-3
        self.speed_y=3
def move(self):
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
def collide(self):
    if self.rect.x<0 or self.rect.x>screensize_x-self.width:
        self.speed_x=-1*self.speed_x
    if self.rect.y<0 or self.rect.y>screensize_y-self.height:
        self.speed_y=-1*self.speed_y
def gameover(self):
    if self.rect.x<0 or self.rect.x>screensize_x-paddle_width:
        self.rect.x=screensize_x/2
        return True
    else:
        return False
#------------Sprite initialization----------------
balls = pygame.sprite.Group()
allsprites = pygame.sprite.RenderPlain()
player2=Player(0,0)
player1=Player(screensize_x-paddle_width,0)
ball=Ball()
balls.add(ball)
allsprites.add(player1,player2,ball)
#-----------Game Initialization------------------
rungame=True
gameover=False
#-----------Main Program Loop---------------------
while rungame:
    screen.fill(screen_color)
#----------Events-----------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame=False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player1.speed_y=-4
        if event.key == pygame.K_DOWN:
            player1.speed_y=4
        if event.key == pygame.K_w:
            player2.speed_y=-4
        if event.key == pygame.K_s:
            player2.speed_y=4
        if event.key == pygame.K_SPACE:
            gameover=False
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            player1.speed_y=0
        if event.key == pygame.K_DOWN:
            player1.speed_y=0
        if event.key == pygame.K_w:
            player2.speed_y=0
        if event.key == pygame.K_s:
            player2.speed_y=0
#---------Game Logic-----------------------------
if not gameover:
    player1.move()
    player2.move()
    gameover=ball.gameover()
    ball.move()
    player1.collide()
    player2.collide
    ball.collide()
if gameover:
    text=font.render("Game Over: Press Space",True,white)
    text_position=text.get_rect(centerx=background.get_width()/2)
    text_position.top=250
    screen.blit(text,text_position)
if pygame.sprite.spritecollide(player1,balls,False):
    ball.speed_x=-1*ball.speed_x
if pygame.sprite.spritecollide(player2,balls,False):
    ball.speed_x=-1*ball.speed_x
#------------Update Drawings-------------------------
    allsprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
