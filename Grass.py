import pygame
from pygame.locals import *
import random
class Grass(pygame.sprite.Sprite):
    def __init__(self,openAnimation):
        super(Grass,self).__init__()
        self.images = []
        self.image = pygame.image.load('Images/Grass/Grass.png')
        openAnimation(self,'Grass',self.images,'.png','Images/Grass/',5)
        self.rect = self.image.get_rect()
        self.index = 0
        self.AnimSpeed = 17
    def update(self,AnimPlay):
        AnimPlay(self,self.images,self.AnimSpeed)
