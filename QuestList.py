import pygame
from pygame import *
class QuestList():
    def __init__(self):
        self.quests = []
        self.open = False
    def update(self,pk,screen,quests):
        if pk[K_q] and self.open == False:
            self.open = True
        elif pk[K_q] and self.open == True:
            self.open = False
        if self.open == True:
            screen.fill((255,255,0))
            x,y = 0,0
            for quest in quests:
                screen.blit(quest.txt,(x,y))
                screen.blit(quest.txtnum,(x,y + 30))
                y += 60
