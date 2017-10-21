import pygame
from pygame import *
class Button(pygame.sprite.Sprite):
    def __init__(self,TOB,image):
        self.Text_On_Button = TOB
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
