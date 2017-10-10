 #In developing
import pygame
import info as inf
from pygame import *
class PlayersLevel():
    def __init__(self):
        self.image = pygame.image.load('Images/Levels/LevelBar.png')
        self.miniimage = pygame.image.load('Images/Levels/Peace.png')
        self.open = False
        self.level = 0
        self.maxlevel = 230
        self.levelcost = 100
        self.PowerUpPoints = 0
        self.index = 0
    def level_up(self,AnimPlay,screen,txtmaker):
        AnimPlay(self,self.level_up_images,4)
        screen.blit(txtmaker(str(inf.PlayerLevel + 1)),(inf.screenwidth // 2 , inf.screenheight // 2))
    def update(self,screen):
        screen.blit(self.image,(x,y))
        x = self.rect.left + 4
        y = self.rect.top + 4
        for i in range(inf.PlayerExpirence//(self.levelcost // 100)):
            screen.blit(self.miniimage,(x + (i * 3),y))
        if inf.PlayerExpirence >= self.levelcost and not self.level >= self.maxlevel:
            self.level_up()
            inf.PlayerLevel += 1
            self.PowerUpPoints += 1
            self.levelcost = (self.level + 1) * self.levelcost
            inf.PlayerExpirence = 0
