import pygame, sys
from random import randrange, choice
from pygame.locals import *
from math import *
from bulletTrajClass import bullet
from vecClass import vector


##this is the code. As of now it doesn't work i need help trying to figure out what's wrong.


class suiciders(pygame.sprite.Sprite):

    def __init__(self, pos, surf, vector, speed, size):

        pygame.sprite.Sprite.__init__(self)

        self.SURF = surf
        self.SIZE = size
        self.POS = pos
        self.VECTOR = vector
        self.SPEED = speed


        self.image = pygame.Surface((self.SIZE,self.SIZE), flags=SRCALPHA, depth=32)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos.vX
        self.rect.y = pos.vY

        self.met = pygame.image.load("enemy_1.png").convert_alpha()
        self.met = pygame.transform.scale(self.met, (self.SIZE, self.SIZE))
        self.image.blit(self.met, (0, 0))


    def resizeImage(self, x, y, xPOS, yPOS):
        self.image = pygame.transform.scale(self.image, (x, y))
        self.rect = self.image.get_rect()
        self.rect.x = xPOS
        self.rect.y = yPOS


    def __moveSuicide(self, pos, vec, speed):

        if pos.vX < vec.vX:
            pos.vX += speed
        if pos.vX > vec.vX:
            pos.vX -= speed
        if pos.vY < vec.vY:
            pos.vY += speed
        if pos.vY > vec.vY:
            pos.vY -= speed
            
        return pos


    def __changePOS(self, pos):

        self.POS = vector(pos.vX, pos.vY)
        self.rect.x = pos.vX
        self.rect.y = pos.vY


    def displaySuicider(self):
        
        self.__changePOS(self.__moveSuicide(self.POS, self.VECTOR, self.SPEED))
        self.SURF.blit(self.image, (self.POS.vX - self.SIZE, self.POS.vY - self.SIZE))
