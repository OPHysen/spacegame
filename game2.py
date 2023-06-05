import imp
from pickle import TRUE
import pygame
import sys
from pygame import mixer
import os

pygame.init()
mixer.init()
pygame.display.set_caption("SPACESHİP")

#FİLES
spaceship =pygame.image.load(f"spaceship.png")
spaceship2 = pygame.image.load("D:\PYTHON2\ewpygame\spaceship2.png")
spaceshipd = pygame.image.load("D:\PYTHON2\ewpygame\spaceshipd.png")
background =pygame.image.load("D:\PYTHON2\ewpygame\\background.jpg")
spaceshipback = pygame.image.load("D:\PYTHON2\ewpygame\spaceshipback.png")
gunphoto = pygame.image.load("D:\PYTHON2\ewpygame\gun.png")
enemy = pygame.image.load("D:\PYTHON2\ewpygame\enemy.png")
blast = pygame.image.load(r"D:\PYTHON2\ewpygame\ulast.png")
imageanimaton =[pygame.image.load("D:\PYTHON2\ewpygame\spaceshipd.png"), pygame.image.load("D:\PYTHON2\ewpygame\spaceshipd2.png")]
spaceship_copy = pygame.image.load("D:\PYTHON2\ewpygame\spaceship copy.png")
#SOUNDS
mixer.music.load("D:\PYTHON2\ewpygame\mainspace.mp3")
gunsound = mixer.Sound("D:\PYTHON2\ewpygame\gun.mp3")
mixer.music.play()

#SCREEN
screen = (1000, 600)
realscreen = pygame.display.set_mode(screen)


def gun(x, y):
    global animgun
    animgun = 1
    gunsound.play()
    realscreen.blit(gunphoto, (x, y))
    

#SPACESHIP
x = 5
y = 5
yon = 1
spaceship_animation = 0

#GUN
animgun = 0
gunx = x

#ENEMY
enemyx = 1000
enemyy = 300
enemy_situation = 1
enemy_move = 1
enemyx_route = 1

#POINT AND POINT TEXT FONT
font= pygame.font.SysFont("italic",50)
point2 = 0

#FPS
clock = pygame.time.Clock()


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        clock.tick(60)
        realscreen.blit(background,(0,0))
        realscreen.blit(spaceship,(x,y))

        #ENEMY MOVEMENT
        if enemy_situation == 1:
                if 100 > enemyy or enemyy > 400 :
                    enemy_move *= -1
                if enemyx == 100:
                    enemyx_route *= -1
                if enemyx == 1050:
                    enemyx_route *= -1
                enemyy += 2 *enemy_move
                enemyx -= 2 *enemyx_route
                realscreen.blit(enemy, (enemyx,enemyy))
            
        
        key_input = pygame.key.get_pressed()   
        if event.type == pygame.MOUSEBUTTONDOWN:
            x -= 5
            yon = 0
            spaceship = spaceshipback
        elif key_input[pygame.K_d]:
            x += 5
            yon = 1
            spaceship= spaceship_copy
            if spaceship_animation > 1:
                spaceship_animation = 0
            realscreen.blit(imageanimaton[spaceship_animation],(x,y))
        elif key_input[pygame.K_w]:
            y -= 5
            if yon == 0:
                spaceship = spaceshipback
            else:
                spaceship = spaceship2
        elif key_input[pygame.K_s]:
            y += 5
            if yon == 0:
                spaceship = spaceshipback
            if yon == 0:
                spaceship = spaceshipback
            else:
                spaceship =pygame.image.load("D:\PYTHON2\ewpygame\spaceship.png")
        elif key_input[pygame.K_SPACE] :
                gun(gunx+120, y+50)
        
        #GUN        
        if animgun == 1:
            gun(gunx+120,y+50)
            if gunx < 800:
                gunx += 20
            #ENEMY DESTROYED
            if enemyx-40<gunx <enemyx-5 and enemy_situation == 1 and (enemyy-20 < y < enemyy+20):
                point2 += 10
                enemy= pygame.image.load(r"D:\PYTHON2\ewpygame\ulast.png")
                realscreen.blit(enemy, (enemyx-50,enemyy-70))
                enemy_situation = 0
            
            elif gunx > 800:
                gunx = x
                animgun = 0
        #POINT TEXT
        point = font.render(f"{point2}" ,1,(255,0,0))
        if enemy_situation ==0:
            enemy_situation = 1
            enemyx = 1000
            enemyy = 300
            enemy = pygame.image.load("D:\PYTHON2\ewpygame\enemy.png")
        spaceship_animation += 1
        realscreen.blit(point, (900,50))
        pygame.display.update()