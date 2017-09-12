import pygame
from pygame.locals import *
import random
class Doors(pygame.sprite.Sprite):
    def __init__(self):
        super(Doors,self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images\Door\Wallinv.png').convert())
        self.images.append(pygame.image.load('Images\Door\Wallinv2.png').convert())
        self.images.append(pygame.image.load('Images\Door\Wallinvno.png').convert())
        self.images.append(pygame.image.load('Images\Door\Wallinvyes.png').convert())
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.open = False
