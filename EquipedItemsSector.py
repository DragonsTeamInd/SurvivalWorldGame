import pygame
from pygame import *
class EquipedItemsSector():
    def __init__(self):
        self.image = pygame.image.load('Images/Inventory/EquipList.png').convert_alpha()
        self.ArmorImage = None
        self.MeeleWeaponImage = None
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 36 * 3
    def SetEquipList(self,Armors,MeeleWeapon):
        for Armor in Armors:
            if Armor.equpe == True:
                self.ArmorImage = Armor.EquipIco
        for MW in MeeleWeapon:
            if MW.equpe == True:
                self.MeeleWeaponImage = MW.EquipIco
    def EquipListBlit(self,Armors,screen,MeeleWeapon):
        self.SetEquipList(Armors,MeeleWeapon)
        screen.blit(self.image,self.rect)
        if not self.ArmorImage == None:
            screen.blit(self.ArmorImage,(self.rect.left + 120,self.rect.top + 7))
        if not self.MeeleWeaponImage == None:
            screen.blit(self.MeeleWeaponImage,(self.rect.left + 120,self.rect.top + 90))
