import pygame
from pygame.locals import *
import random
class Walls(pygame.sprite.Sprite):
    def __init__(self):
        super(Walls,self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images\Wall\Wall.png').convert())
        self.images.append(pygame.image.load('Images\Wall\Wallno.png').convert())
        self.images.append(pygame.image.load('Images\Wall\Wallyes.png').convert())
        self.images[0].set_colorkey((255,255,255))
        self.images[1].set_colorkey((255,255,255))
        self.images[2].set_colorkey((255,255,255))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
