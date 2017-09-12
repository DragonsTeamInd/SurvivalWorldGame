import pygame
from pygame import *
class Cursour(pygame.sprite.Sprite):
    def __init__(self):
        super(Cursour,self).__init__()
        self.image = pygame.image.load('Images/Kursors/InvisibC.png')
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
    def update(self):
        x,y = pygame.mouse.get_pos()
        self.rect.left = x
        self.rect.top = y
