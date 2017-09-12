import pygame
from pygame.locals import *
class Trees(pygame.sprite.Sprite):
    def __init__(self):
        super(Trees,self).__init__()
        self.image = pygame.image.load('Images\Tree\Tree.png')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
