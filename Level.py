import pygame
import info as inf
from pygame import *
class PlayersLevel():
    def __init__(self):
        self.image = pygame.image.load('Images/Levels/LevelBck.png')
        self.rect = self.image.get_rect()
        self.open = False
        self.level = 0
        self.maxlevel = 230
        self.levelcost = 100
        self.PowerUpPoints = 0
    def update(self):
        if inf.PlayerExpirence >= self.levelcost and not self.level >= self.maxlevel:
            self.level += 1
            self.PowerUpPoints += 1
            self.levelcost = (self.level + 1) * self.levelcost
