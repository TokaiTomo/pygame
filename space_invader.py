import pygame
import random
import os
import math
#=====Consistent=======
SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE=27
#=====init=========
pygame.init()
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#=====background======
background=pygame.image.load(os.path.join(BASE_DIR,'background.png'))
icon=pygame.image.load(os.path.join(BASE_DIR,'ufo.png'))
player=pygame.image.load(os.path.join(BASE_DIR,'player.png'))
bullet=pygame.image.load(os.path.join(BASE_DIR,'bullet.png'))

pygame.display.set_caption('Space Invader Game👾')
pygame.display.set_icon(icon)
#======Player=====
playerX=PLAYER_START_X
playerY=PLAYER_START_Y
playerX_change=0
#=======Enemy=======
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyImg.append(
        pygame.image.load(os.path.join(BASE_DIR,'ufo.png'))
    )
    enemyX.append(random.randint(0,SCREEN_WIDTH-64))
    enemyY.append(random.randint(0,ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
#=======Bullet=======   