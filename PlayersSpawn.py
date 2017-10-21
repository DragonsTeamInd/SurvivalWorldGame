import pygame
import info as inf
from pygame import *
class PlayersSpawn():
    def SpawnOnGround(self,ground,player):
        for gr in ground:
            if abs(gr[0] - inf.screenwidth // 2) <= 72:
                player.rect.top = gr[1] - (72 + inf.Ground_Block_Height)
