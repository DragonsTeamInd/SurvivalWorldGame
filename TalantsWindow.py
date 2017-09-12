import pygame
from pygame import *
class TalantsWindow():
    def __init__(self):
        self.bck = pygame.image.load('images/BackGrounds/TalantsBack.png')
        self.open = False
    def update(self,talants,pk,screen):
        if pk[K_t] and self.open == False:
            self.open = True
        elif pk[K_t] and self.open == True:
            self.open = False
        if self.open == True:
            screen.blit(self.bck,(0,0))
            for talant in talants:
                screen.blit(talant.image,talant.rect)
