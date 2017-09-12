import pygame
from pygame import *
from Talant import Talant
import info as inf
from DataSave_And_DataOpen import opendata,savedata
class Talants():
    def __init__(self):
        self.talants = []
        self.talantsnum = 2
        self.talantsimages = ['images/Talants/T1.png','images/Talants/T2.png']
        self.talantsbonustype = ['damagebonus','damagebonus']
        self.talantsbonusnums = [2,4]
        self.talantsPointNeed = [1,2]
        self.openedtalants = []
        self.closedtalants = []
        self.opened = [0]
        self.save_file_name = 'TalantsParameters.txt'
    def opendata(self):
        opendata(self.save_file_name,self.opened)
        for i in self.closedtalants[0 : self.opened[0]]:
            self.openedtalants.append(i)
        for i in self.closedtalants[0 : self.opened[0]]:
            self.closedtalants.remove(i)
    def savedata(self):
        savedata(self.opened,self.save_file_name)
    def CreateTalants(self):
        for i in range(self.talantsnum):
            imageroad = self.talantsimages[i]
            place = i + 1
            bonustype = self.talantsbonustype[i]
            bonusnum = self.talantsbonusnums[i]
            PointNeed = self.talantsPointNeed[i]
            new_talant = Talant(imageroad,place,bonustype,bonusnum,PointNeed)
            self.closedtalants.append(new_talant)
            self.talants.append(new_talant)
        self.opendata()
    def opentalant(self,mouse,event):
        for ctalant in self.closedtalants:
            if pygame.sprite.collide_rect(mouse,ctalant):
                if event.type == pygame.MOUSEBUTTONUP:
                    if inf.PowerUpPoints >= ctalant.PointNeed:
                        self.openedtalants.append(ctalant)
                        self.closedtalants.remove(ctalant)
                        self.opened[0] += 1
                        inf.PowerUpPoints -= ctalant.PointNeed
                        self.savedata(self)
    def update(self,player):
        damagebonus = 0
        for otalant in self.openedtalants:
            if otalant.bonustype == 'damagebonus':
                damagebonus += otalant.bonusnum
        player.damagebonus = damagebonus
