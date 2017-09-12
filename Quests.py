import pygame
from pygame import *
class Quest(pygame.sprite.Sprite):
    def __init__(self,txt,Questq,num):
        super(Quest,self).__init__()
        self.nownum = 0
        Text = txt
        TextFont = pygame.font.SysFont('None', 30)
        self.txt = TextFont.render(Text, 0, (0,0,5))
        Text = str(self.nownum) + ' / ' + str(num)
        TextFont = pygame.font.SysFont('None', 30)
        self.txtnum = TextFont.render(Text, 0, (0,0,5))
        self.Num = num
        self.complite = False
        self.Quest = Questq
    def update(self):
        if self.nownum == self.Num:
            self.complite = True
        Text = str(self.nownum) + ' / ' + str(self.Num)
        TextFont = pygame.font.SysFont('None', 30)
        self.txtnum = TextFont.render(Text, 0, (0,0,5))
