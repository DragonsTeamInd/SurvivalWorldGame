import pygame
import info as inf
from pygame import *
class MeeleWeapon(pygame.sprite.Sprite):
    def __init__(self,damage,image,ico,EquipIco,imageT,openAnimation,Wave):
        super(MeeleWeapon,self).__init__()
        self.images = []
        self.imagesT = []
        openAnimation(self,image,self.images,'.png','Images/Weapons/',5)
        openAnimation(self,imageT,self.imagesT,'.png','Images/Weapons/',5)
        self.image = self.images[0]
        self.ico = pygame.image.load(ico).convert_alpha()
        self.EquipIco = pygame.image.load(EquipIco).convert_alpha()
        self.Damage = damage
        self.Wave = Wave
        self.rect = self.image.get_rect()
        self.equpe = False
        self.canequpe = True
        self.ininventory = True
        self.icoininventory = True
        self.addicoininventory = True
        self.candelete = True
        self.id = None
        self.type = 'EquipedItemMeeleWeapon'
        self.index = 0
        self.playanim = False
        self.animL = 0
        self.animR = 0
    def MouseLeftorRight(self,player):
        x,y = pygame.mouse.get_pos()
        if player.Leftside == True:
            self.image = self.imagesT[0]
            return 16
        elif player.Leftside == False:
            self.image = self.images[0]
            return 0
    def AnimLeftorRight(self,AnimPlay,player):
        if self.playanim == True:
            x,y = pygame.mouse.get_pos()
            if player.Leftside == True:
                AnimPlay(self,self.imagesT,1)
                self.animL += 1
            elif player.Leftside == False:
                AnimPlay(self,self.images,1)
                self.animR += 1
        if self.animR >= 5 or self.animL >= 5:
            self.playanim = False
            self.animR = 0
            self.animL = 0
    def Attak(self,enemies,player):
        if self.equpe == True:
            self.playanim = True
            for Enemy in enemies:
                if pygame.sprite.collide_rect(self,Enemy):
                    Enemy.health -= self.Damage + player.damagebonus
                    if self.rect.left > player.rect.left:
                        Enemy.rect.left += self.Wave
                    else:
                        Enemy.rect.left -= self.Wave
                    Enemy.rect.top -= 5
    def update(self,player,all_sprites,invblock,AnimPlay,screen):
        if self.equpe == True:
            self.ininventory = False
            all_sprites.add(self)
            left = self.MouseLeftorRight(player)
            self.AnimLeftorRight(AnimPlay,player)
            self.rect.left = player.rect.left - left
            self.rect.top = player.rect.top - 16
            screen.blit(self.image,self.rect)
            player.damage = self.Damage
        else:
            self.ininventory = True
