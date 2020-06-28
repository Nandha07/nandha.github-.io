import pygame
from pygame import mixer
import math
import random

pygame.init()
#clock=pygame.time.Clock()
#game window
screen =pygame.display.set_mode((800,600))

#background

background=pygame.image.load("background.png")

#background sound
#mixer.music.load("background.wav")
#mixer.music.play(-1)


#icon
pygame.display.set_caption("SPACE INVADER")
i = pygame.image.load("ufo.png")
pygame.display.set_icon(i)

#player
playerimg=pygame.image.load("space-invaders.png")
playerx=370
playery=480
playerx_change=0

#enemy
enemyimg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies=6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyx.append (random.randint(0,735))
    enemyy.append (random.randint(50,150))
    enemyx_change.append(4)
    enemyy_change.append(40)
#bullets
bulletsimg=pygame.image.load("bullet.png")
bulletsx=0
bulletsy= 480
bulletsx_change=0
bulletsy_change=10
bullet_state="ready"

#score
score_value=0
font=pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10

#gameover textx
over_font=pygame.font.Font("freesansbold.ttf",64)

def show_score(x,y):
    score=font.render("score:"+str (score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullets(x,y):
    global bullet_state
    bullet_state="fire"

    screen.blit(bulletsimg,(x+16,y+10))
def iscollison(enemyx,enemyy,bulletsx,bulletsy):
    distance=math.sqrt(math.pow(enemyx-bulletsy,2)+math.pow(enemyy-bulletsy,2))
    if distance <27:
       return True
    else:
       return False


running=True
while running:
    screen.fill((75,23,255))
     #background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
          #if key stoke is pressed
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                playerx_change = -5
             if event.key == pygame.K_RIGHT:
                playerx_change = +5
             if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    #bullets_sound=mixer.sound("thunder.wav")
                    #bullets_sound.play()
                    bulletsx=playerx
                    fire_bullets(bulletsx,bulletsy)

        if event.type ==pygame.KEYUP:
             if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT:
                playerx_change=0
    playerx +=playerx_change
    if playerx <=0:
        playerx=0
    elif playerx >=736:
        playerx=736
    #enemy movement
    for i in range(num_of_enemies):
        if enemyy[i]>460:
            for j in range(num_of_enemies):
                enemyy[j]=2000
            game_over_text()
            break
        enemyx[i] +=enemyx_change[i]
        if enemyx[i] <=0:
            enemyx_change[i]=4
            enemyy[i]+=enemyy_change[i]
        elif enemyx[i] >=736:
            enemyx_change[i]=-4
            enemyy[i]+=enemyy_change[i]
        #iscollison
        collison=iscollison(enemyx[i],enemyy[i],bulletsx,bulletsy)
        if collison:
            #explosion_sound=mixer.sound("thunder.wav")
            #explosion_sound.play()
            bulletsy=480
            bullet_state="ready"
            score_value+=1

            enemyx[i]=random.randint(0,735)
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i],i)
        #bullets movement
    if bulletsy<=0:
         bulletsy=480
         bullet_state="ready"

    if bullet_state is  "fire":
        fire_bullets(playerx,bulletsy)
        bulletsy -=bulletsy_change


    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()
