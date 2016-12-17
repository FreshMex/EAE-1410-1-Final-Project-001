import pygame, sys
from pygame.locals import *
from vecClass import vector
from math import *

class ship(pygame.sprite.Sprite):

    def __init__(self, pos, size, graphic, surf):

        pygame.sprite.Sprite.__init__(self)

        self.WIDTH = size[0]
        self.HEIGHT = size[1]
        self.xPOS = pos.vX
        self.yPOS = pos.vY
        self.POS = pos
        self.SURF = surf
        self.GRAPHIC = graphic

        self.image = pygame.Surface((self.WIDTH, self.HEIGHT), flags=SRCALPHA, depth=32)
        self.image.fill((0, 0, 0, 0))
        self.graphic1 = pygame.image.load(self.GRAPHIC).convert_alpha()
        self.graphic1 = pygame.transform.scale(self.graphic1, (self.WIDTH, self.HEIGHT))
        self.image.blit(self.graphic1, (0, 0))
        self.tempIMAGE = self.image
        
        self.rect = self.image.get_rect()
        self.rect.x = self.xPOS
        self.rect.y = self.yPOS

    def rotateCenter(self, angle):

        self.image = pygame.transform.rotate(self.tempIMAGE, angle)
        w, h = self.image.get_size()
        self.POS = vector(self.xPOS - w//2, self.yPOS - h//2)
        self.rect = self.image.get_rect()
        self.rect.x = self.POS.vX
        self.rect.y = self.POS.vY

    def changeShipPos(self, pos, vec, speed):
        pos += vec * speed
        return pos
    def displayShip(self):
        
        #self.SURF.blit(self.image, (self.rect.x, self.rect.y))
        self.SURF.blit(self.image, (self.POS.vX - self.WIDTH//2, self.POS.vY - self.HEIGHT//2))
        
