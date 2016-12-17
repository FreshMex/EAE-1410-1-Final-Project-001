##nova_blaster_main.py
##12/13/16
##Jacob Gillars

import pygame, sys
from random import randrange, choice
from pygame.locals import *
from math import *
from bulletTrajClass import bullet
from vecClass import vector
from suicider import suiciders
from shipClass import ship

ship1 = 'ship_idle.png'
ship2 = 'ship_idle_damaged.png'
ship3 = 'ship_moving.png'
ship4 = 'ship_moving_damaged.png'
bulImg1 = 'player_attack_normal.png'
bulImg2 = 'player_attack_special.png'
shipImg = ship1
pygame.init()
FPSCLOCK = pygame.time.Clock()
bulletFlySpeed = 5
screen = pygame.display.set_mode((1200,900),0,32)

SPSpos = vector(600,450)
SPSrot = 0
SPSize = (108,108)
bulletList = pygame.sprite.Group()
suicideLIST = pygame.sprite.Group()
STARTspPOS = vector(600,450)
MAX_STARS  = 250
STAR_SPEED = 2
moving = False

def init_stars(screen):
  global stars
  stars = []
  for i in range(MAX_STARS):
    star = [randrange(0,screen.get_width() - 1),randrange(0,screen.get_height() - 1),choice([1,2,3])]
    stars.append(star)
    
def rotateCenter(image, angle):
  rect = image.get_rect()
  rotateImg = pygame.transform.rotate(image, angle)
  rotateRect = rect.copy()
  rotateRect.center = rotateImg.get_rect().center
  rotateImg = rotateImg.subsurface(rotateRect).copy()
  return rotateImg

def move_and_draw_stars(screen):
##  global x
##  x = 0
##  global y
##  y = 0
  global stars
  for star in stars:
##    if y == 1 and moving == True:
##      star[1] += star[2]
##    elif y == -1 and moving == True:
##      star[1] -= star[2]
##    if x == -1 and moving == True:
##      star[0] += star[2]
##    elif x == 1 and moving == True:
##      star[0] -= star[2]
##    if star[1] >= screen.get_height():
##      star[1] = 0
##      star[0] = randrange(0,639)
##      star[2] = choice([1,2,3])
##    elif star[1] <= 0:
##      star[1] = screen.get_height()
##      star[0] = randrange(0,639)
##      star[2] = choice([1,2,3])
##    if star[0] >= screen.get_width():
##      star[0] = 0
##      star[1] = randrange(0,639)
##      star[2] = choice([1,2,3])
##    elif star[0] <= 0:
##      star[0] = screen.get_width()
##      star[1] = randrange(0,639)
##      star[2] = choice([1,2,3])
    if star[2] == 1:
      color = (60,60,60)
    elif star[2] == 2:
      color = (145,145,145)
    elif star[2] == 3:
      color = (200,200,200)
    screen.fill(color,(star[0],star[1],star[2],star[2]))
    
##def attack(pwr, rotationDIRcc):
##  powerLvl = pwr
##  shotTraj = ()
##  shotDev = 20.0
##  bulletCount = 0 
##  if powerLvl == 1:
##    shotTraj = rotationDIRcc
##    bulletCount = 1
##  elif powerLvl == 2:
##    shotTraj = (rotationDIRcc, rotationDIRcc + shotDev, rotationDIRcc - shotDev)
##    bulletCount = 2
##  elif powerLvl == 3:
##    shotTraj = (rotationDIRcc, rotationDIRcc + shotDev, rotationDIRcc - shotDev, rotationDIRcc + (2*shotDev), rotationDIRcc - (2*shotDev))
##    bulletCount = 3
##  elif powerLvl == 4:
##    shotTraj = (rotationDIRcc, rotationDIRcc + shotDev, rotationDIRcc - shotDev, rotationDIRcc + (2*shotDev), rotationDIRcc - (2*shotDev), rotationDIRcc + (3*shotDev), rotationDIRcc - (3*shotDev))
##    bulletCount = 4
##  elif powerLvl == 5:
##    shotTraj = (rotationDIRcc, rotationDIRcc + shotDev, rotationDIRcc - shotDev, rotationDIRcc + (2*shotDev), rotationDIRcc - (2*shotDev), rotationDIRcc + (3*shotDev), rotationDIRcc - (3*shotDev), rotationDIRcc + (4*shotDev), rotationDIRcc - (4*shotDev))
##    bulletCount = 5
##  return shotTraj, bulletCount

def makeSuiciders():
    numSuicide = 5

    while numSuicide > 0:
        randx = randrange(-1000, 1200 + 1000)
        randy = randrange(-1000, 900 + 1000)

        if not (randx > 0 and randx < 1200 and randy > 0 and randy < 900):
            v1 = vector(randx, randy)
            v2 = vector.fromPoints((randx, randy), (SPSpos.vX, SPSpos.vY))

            suicideLIST.add(suiciders(v1, screen, v2, 5.0, 100))
            numSuicide -= 1

def main():
  SPShip = pygame.image.load(ship1).convert_alpha()
  tempVector = vector.fromPoints((STARTspPOS.vX, STARTspPOS.vY),(STARTspPOS.vX + 0, STARTspPOS.vY - 10))
  tempVector = tempVector.normalizeV2()
  pygame.display.set_caption("Nova Blaster")
  clock = pygame.time.Clock()
  score = 0
  health = 3
  spriteROT = 0.0
  drawSPS = (600,450)
  global moving
  moving = False
  left = False
  right = False
  shooting = False
  shotDev = []
  moveX = 570
  moveY = 425
  global speed
  speed = 0
  global topSpeed
  topSpeed = 30
  global accelaration
  accelaration = 1
  init_stars(screen)
  rotationDIRcc = 0
  power = 1
  S1 = ship(SPSpos, SPSize, ship1, screen)
  makeSuiciders()
  while True: 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        return
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit()
          return
        elif event.key == K_w:
          moving = True
        elif event.key == K_d:
          rotationDIRcc = -3.0
        elif event.key == K_a:      
          rotationDIRcc = 3.0
        elif event.key == K_SPACE:
          shipImg = ship2
          bulletList.add(bullet(drawBul, screen, vector1, bulletFlySpeed, 20, spriteROT, bulImg1))
      elif event.type == KEYUP:
        if event.key == K_w:
          moving = False
        elif event.key == K_d:
          rotationDIRcc = 0
        elif event.key == K_a:
          rotationDIRcc = 0
        elif event.type == K_SPACE:
          pass
    while rotationDIRcc > 359:
      rotationDIRcc -= 360
    while rotationDIRcc < 0:
      rotationDIRcc += 360
    if len(suicideLIST) < 1:
            makeSuiciders()
    spriteROT += rotationDIRcc
    xRot = cos(radians(spriteROT))
    yRot = sin(-radians(spriteROT))
    if moving:
      speed = 3
      moveY -= int(speed * xRot)
      moveX += int(speed * yRot)
    if moveX <= 0:
      moveX = 0
    elif moveX >= 1100:
      moveX = 1100
    if moveY <= 0:
      moveY = 0
    elif moveY >= 800:
      moveY = 800
    suiciderCollisions = pygame.sprite.spritecollide(S1, suicideLIST, True)
    suiciderBulletCollisions = pygame.sprite.groupcollide(suicideLIST, bulletList, True, True)
    for SX in suicideLIST:
        SX.displaySuicider()
    #RotSPS = rotateCenter(SPShip,spriteROT)
    S1.rotateCenter(spriteROT)
    drawSPS = vector(moveX, moveY)
    drawBul = vector(moveX+58,moveY+58)
    screen.fill((0,0,0))
    for b in bulletList:
      if b.rect.x > 0 and b.rect.y > 0 and b.rect.x < 1200 and b.rect.y < 900:
        b.bulBlit()
      else:
        bulletList.remove(b)
    changeShipPos(drawSPS, vector1, speed)
    move_and_draw_stars(screen)
    vector1 = tempVector.rotateV2(-spriteROT)
    #screen.blit(RotSPS,drawSPS)
    S1.displayShip()
    pygame.display.update()
    clock.tick(60)

if __name__ == "__main__": main()
