## spaceSHIPclass.py
## Giovanni Varuola
## 12/16/16

import pygame, sys
from pygame.locals import *
from vecClass import vector
from math import *

class spaceSHIP(pygame.sprite.Sprite):

    def __init__(self, pos, size, surf):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.WIDTH = size[0]
        self.HEIGHT = size[1]
        self.xPOS = pos.vX
        self.yPOS = pos.vY
        self.POS = pos
        self.SURF = surf

        self.image = pygame.Surface((self.WIDTH, self.HEIGHT), flags=SRCALPHA, depth=32)
        self.image.fill((0, 0, 0, 0))
        
        self.rect = self.image.get_rect()
        self.rect.x = self.xPOS
        self.rect.y = self.yPOS

    def update(self, pos):
        self.rect.x = pos.vX
        self.rect.y = pos.vY
        
        
    def displaySpaceSHIP(self):
        
        self.SURF.blit(self.image, (self.rect.x, self.rect.y))
        #self.SURF.blit(self.image, (self.POS.vX - self.WIDTH//2, self.POS.vY - self.HEIGHT//2))
        
