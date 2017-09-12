import pygame
import info as inf
from pygame import *
class Armor(pygame.sprite.Sprite):
    def __init__(self,defens,image,ico,EquipIco,image1,Armors):
        super(Armor,self).__init__()
        self.images = []
        self.images.append(pygame.image.load(image).convert_alpha())
        self.images.append(pygame.image.load(image1).convert_alpha())
        self.image = self.images[0]
        self.ico = pygame.image.load(ico).convert_alpha()
        self.EquipIco = pygame.image.load(EquipIco).convert_alpha()
        self.Defense = defens
        self.rect = self.image.get_rect()
        self.equpe = False
        self.canequpe = True
        self.ininventory = True
        self.icoininventory = True
        self.addicoininventory = True
        self.candelete = True
        self.id = None
        self.type = 'EquipedItemArmor'
        if not self in Armors:
            Armors.append(self)
    def MouseLeftorRight(self,player):
        x,y = pygame.mouse.get_pos()
        if player.Leftside == True:
            self.image = self.images[1]
        elif player.Leftside == False:
            self.image = self.images[0]
    def update(self,player,all_sprites,invblock,screen,Armors):
        if self.equpe == True:
            self.ininventory = False
            screen.blit(self.image,self.rect)
            self.MouseLeftorRight(player)
            self.rect.left = player.rect.left
            self.rect.top = player.rect.top
            player.defens = self.Defense
        else:
            self.ininventory = True
