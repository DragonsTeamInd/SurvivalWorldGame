import pygame
import info as inf
from pygame import *
class ItemDrop(pygame.sprite.Sprite):
    def __init__(self,image,index):
        super(ItemDrop,self).__init__()
        self.image = image
        self.types = [inf.wool]
        self.index = index
        self.rect = self.image.get_rect()
    def update(self,ground,player,screen):
        screen.blit(self.image,self.rect)
        if not pygame.sprite.spritecollide(self,ground,False,False):
            self.rect.top += 2
        if pygame.sprite.collide_rect(self,player):
            self.types[self.index] += 1
            self.kill()
