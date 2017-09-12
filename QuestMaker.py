import pygame
from Quests import Quest
from pygame import *
class QuestMaker():
    def __init__(self):
        self.questsnum = 2
        self.questsq = ['Craft Armor','Craft Sword']
        self.queststxt = ["It's time to upgrade! Craft Armor","It's time to kill your enemies! Craft Sword"]
        self.questsnums = [1,1]
    def QuestCreate(self,quests):
        for index in range(self.questsnum):
            quest = Quest(self.queststxt[index],self.questsq[index],self.questsnums[index])
            quests.add(quest)
