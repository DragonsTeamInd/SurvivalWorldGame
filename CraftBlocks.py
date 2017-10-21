import pygame
import info as inf
import Groups
import copy
from Armor import Armor
from MeeleWeapon import MeeleWeapon
from pygame import *
class CraftBlocks(pygame.sprite.Sprite):
    def __init__(self,Item,Groups,openAnimation):
        super(CraftBlocks,self).__init__()
        self.Selectedimage = pygame.image.load('images/CraftingIcons/Selected.png').convert_alpha()
        self.items = dict()
        self.items['0'] = 'Images/CraftingIcons/LeatherArmorCraftIco.png'
        self.items['0P'] = 500
        self.items['0RT'] = ['wood']
        self.items['0T'] = Armor(6,'Images/Armor/LeatherArmor.png','Images/Inventory/ArmorIco.png','Images/Armor/EquipedLeatherArmor.png','Images/Armor/LeatherArmor1.png',Groups.Armors)
        self.items['0G'] = Groups.Armors
        self.items['0AiAL'] = False
        self.items['Armor'] = 'Images/CraftingIcons/LeatherArmorCraftIco.png'
        self.items['1'] = 'Images/CraftingIcons/CommonSwordCraftIco.png'
        self.items['1RT'] = ['wood']
        self.items['1P'] = 5
        self.items['1T'] = MeeleWeapon(10,'Sword','Images/Inventory/SwordIco.png','Images/Armor/EquipedSword.png','SwordT',openAnimation,15)
        self.items['1G'] = Groups.MeeleWeapon
        self.items['1AiAL'] = False
        self.recoursetype = self.items[Item + 'RT']
        self.prise = self.items[Item + 'P']
        self.Num = Item
        self.type = self.items[Item + 'T']
        self.Group = self.items[Item + 'G']
        self.AiAL = self.items[Item + 'AiAL']
        self.image = pygame.image.load(self.items[Item])
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.craft = False
    def update(self,Mouse,Groups,event,screen,Resourses):
        if inf.IsCraftWindowIsOpen == True:
            if pygame.sprite.collide_rect(self,Mouse):
                screen.blit(self.Selectedimage,self.rect)
                if event.type == MOUSEBUTTONDOWN:
                    for rt in self.recoursetype:
                        for resourse in Resourses:
                            self.craft = False
                            if rt == resourse.crafttype:
                                if resourse.count >= self.prise:
                                    resourse.count -= self.prise
                                    self.craft = True
                    if self.craft == True:
                        new_item = copy.copy(self.type)
                        inf.object = new_item
                        if self.AiAL == True:
                            Groups.all_sprites.add(new_item)
                        self.Group.append(new_item)
                        inf.IsCraftWindowIsOpen = False
                        self.craft = False
