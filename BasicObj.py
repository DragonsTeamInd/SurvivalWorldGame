import pygame
from pygame import *
class BasicObj(pygame.sprite.Sprite):
    def __init__(self,image,rect):
        super(BasicObj,self).__init__()
        self.image = image
        self.rect = self.image.get_rect()
