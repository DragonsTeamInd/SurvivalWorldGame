import pygame
import info as inf
import CraftBlocks as CB
from pygame import *
class CraftWindow():
    def __init__(self):
        self.stroki = 1
        self.size = [['-'] * 2 for i in range(self.stroki)]
        self.bck = pygame.image.load('Images/BackGrounds/BckForCrft.png')
    def CreateCraftWindow(self,craftblocksg,Groups,openAnimation):
        stolb = 0
        for i in self.size:
            stroka = 0
            for q in i:
                new_craftblock = CB.CraftBlocks(str(stroka),Groups,openAnimation)
                new_craftblock.rect.top = stolb * new_craftblock.rect.height
                new_craftblock.rect.left = stroka * new_craftblock.rect.width
                craftblocksg.add(new_craftblock)
                stroka += 1
            stolb += 1
    def render(self,craftblocks,pk,screen):
        if pk[K_e] and inf.IsCraftWindowIsOpen == False:
            inf.IsCraftWindowIsOpen = True
        elif pk[K_e] and inf.IsCraftWindowIsOpen == True:
            inf.IsCraftWindowIsOpen = False
        if inf.IsCraftWindowIsOpen == True:
            screen.blit(self.bck,(0,0))
            for craftblock in craftblocks:
                screen.blit(craftblock.image,craftblock.rect)
            pygame.display.flip()
    def cameraupdate(self,event,craftblocks):
        if inf.IsCraftWindowIsOpen == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                loops = 0
                loops1 = 0
                if event.button == 4:
                    for i in craftblocks:
                        if not loops + 1 >= self.stroki:
                            i.rect.top -= i.rect.height
                    loops += 1
                elif event.button == 5:
                    for i in craftblocks:
                        if not loops1 + 1 >= self.stroki:
                            i.rect.top += i.rect.height
                    loops1 += 1
