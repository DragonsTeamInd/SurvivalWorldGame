import pygame
import info as inf
from pygame.locals import *
import random
class GroundBlock(pygame.sprite.Sprite):
    def __init__(self):
        super(GroundBlock,self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images\Ground\GB.png').convert())
        self.images.append(pygame.image.load('Images\Ground\GB1.png').convert())
        self.images.append(pygame.image.load('Images\Ground\GB2.png').convert())
        self.image = self.images[1]
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.top = inf.screenheight // 2
