import pygame
import info as inf
from pygame import *
class HUD():
    def __init__(self):
        self.image = pygame.image.load('Images/HUD/HelthBar.png').convert_alpha()
        self.miniimage = pygame.image.load('Images/HUD/MiniImage.png').convert()
        self.Health = 0
        self.rect = self.image.get_rect()
        self.rect.top = inf.screenheight - self.rect.height
    def update(self,player,screen):
        self.Health = player.Health
        x = self.rect.left + 95
        y = self.rect.top + 90
        for i in range(self.Health):
            screen.blit(self.miniimage,(x + (i * 2),y))
            screen.blit(self.image,self.rect)
