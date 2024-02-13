#linodes is a server where we can  use to run in a server
import pygame
import math
import random
from pygame import mixer
#initialize  pygame
pygame.init()
#create the screen object but it closes after opening 
screen = pygame.display.set_mode((800,600))

#background
background=pygame.image.load('background.jpeg')
#bg sound
mixer.music.load("backgr.mp3")
mixer.music.play(-1)
#title of the game and Icon
pygame.display.set_caption("Space Invading")
icon=pygame.image.load('image.png')
pygame.display.set_icon(icon)

#player
playerimg=pygame.image.load('player (1).png')
playerx=370
playery=500
playerx_change=0


#Enemy
enemyimg=[]
#we give the values as random because we need our enemy to respawn in different places 
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    #multiple Enemy
    enemyimg.append(pygame.image.load("enemy (1).png"))
    #we give the values as random because we need our enemy to respawn in different places 
    enemyx.append(random.randint(20,700))
    enemyy.append(random.randint(50,150))
    enemyx_change.append(1)
    enemyy_change.append(40)

#bullet
bulletimg=pygame.image.load('buet (1).png')
bulletx=0
bullety=480
bulletx_change=0
bullety_change=1.2
bulletstate="ready"

score=0
font=pygame.font.Font('freesansbold.ttf',32)#in dafont we can download the text file and place the name here
textx=10
texty=10

over_font=pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score1=font.render("Score : "+str(score),True,(0,255,0))
    screen.blit(score1,(x,y))

def game_over_text():
    over_text=over_font.render("Game is Over ",True,(0,255,0))
    screen.blit(over_text,(250,250))

def player(x,y):
    screen.blit(playerimg,(x,y))#blit means draw
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y)) 
def fire_bullets(x,y):
     global bulletstate
     bulletstate="fire"
     screen.blit(bulletimg,(x+16, y+10))

def is_collision(bulletx,bullety,enemyx,enemyy):
     distance=math.sqrt(math.pow((bulletx-enemyx),2)+math.pow((bullety-enemyy),2))
     if distance<37:
         return True
     else:
         return False
#writing a code for events  in which if we press * in the pygame screen it must close
running=True
while running:
    screen.fill((0,0,0))#but it wont change the colour so we add the pygame.display.update() line in every pygame code as we wnt to update score movements and everything
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:#keydown is nothing but pressing the key
            if event.key == pygame.K_LEFT:
                playerx_change=-0.9#it determines n of frames it must move
            if event.key == pygame.K_RIGHT:
                playerx_change=0.9
            if event.key == pygame.K_SPACE:
                 if(bulletstate=="ready"):
                    bullet_sound=mixer.Sound("laser.mp3")
                    bullet_sound.play()
                    bulletx=playerx
                    fire_bullets(bulletx,bullety)
        if event.type==pygame.KEYUP:#keyup is nothing but not pressing the key
                playerx_change=0
                print("key is released")
    playerx +=playerx_change
     
    if playerx <=-20:
         playerx=-20
    elif playerx>=750:
         playerx=750
    
    for i in range(num_of_enemies):
        #Game Over
        if enemyy[i]>480:
            for j in range(num_of_enemies):#this is for removing all the enemies after game is over
                enemyy[j]=2000
            game_over_text()
            break
            
        enemyx[i] +=enemyx_change[i]
        if enemyx[i] <=-20:
            enemyx_change[i]=+0.7
            enemyy[i] += enemyy_change[i]
        elif enemyx[i]>=750:
            enemyx_change[i]=-0.7
            enemyy[i] += enemyy_change[i]
        collision=is_collision(bulletx,bullety,enemyx[i],enemyy[i])
        if collision:
            explosion_sound=mixer.Sound("explosion.mp3")
            explosion_sound.play()
            bullety=480
            bulletstate="ready"
            score+=1

            #we give the values as random because we need our enemy to respawn in different places 
            enemyx[i]=random.randint(20,800)
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i],i)
    if(bullety<=0):
         bullety=480
         bulletstate="ready"
         
    if bulletstate == "fire":
         fire_bullets(bulletx,bullety)
         bullety-=bullety_change

    
    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()
