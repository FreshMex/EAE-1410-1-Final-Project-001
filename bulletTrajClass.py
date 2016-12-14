import pygame, sys
from pygame.locals import *
from vecClass import vector
from math import *
    
class bullet(pygame.sprite.Sprite):

    def __init__(self, pos, surf, vector, speed, size, rot):

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
        self.HSIZE = self.SIZE//2
        self.bul = pygame.image.load('bullets.jpg').convert_alpha()
        self.bul = pygame.transform.scale(self.bul, (self.SIZE//2, self.SIZE))
        self.bul = pygame.transform.rotate(self.bul, rot)
        self.image.blit(self.bul, (0, 0))

    def bulletShift(self, pos, vec, speed):
        
        pos += vec * speed
        return pos

    def changePOS(self, pos):

        self.POS = vector(pos.vX, pos.vY)
        self.rect.x = pos.vX
        self.rect.y = pos.vY

    def bulBlit(self):
        
        self.changePOS(self.bulletShift(self.POS, self.VECTOR, self.SPEED))
        self.SURF.blit(self.image, (self.POS.vX - self.HSIZE, self.POS.vY - self.HSIZE))
