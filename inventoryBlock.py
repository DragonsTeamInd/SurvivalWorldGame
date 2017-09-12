import pygame
from pygame import *
class InventoryBlock(pygame.sprite.Sprite):
    def __init__(self,type):
        super(InventoryBlock,self).__init__()
        self.images = []
        self.images.append(pygame.image.load('Images\Inventory\ZeroItems.png').convert_alpha())
        self.images.append(pygame.image.load('Images\Inventory\WoodItem.png'))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.type = type
        self.item = None
