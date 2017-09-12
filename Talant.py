import pygame
from pygame import *
class Talant(pygame.sprite.Sprite):
    def __init__(self,image,place,bonustype,bonusnum,PointNeed):
        super(Talant,self).__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left = place * self.rect.width + self.rect.width // 4
        self.bonustype = bonustype
        self.bonusnum = bonusnum
        self.PointNeed = PointNeed
