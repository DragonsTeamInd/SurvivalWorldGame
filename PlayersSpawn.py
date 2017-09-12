import pygame
import info as inf
from pygame import *
class PlayersSpawn():
    def SpawnOnGround(self,ground,player):
        for gr in ground:
            if abs(gr.rect.left - inf.screenwidth // 2) <= 72:
                player.rect.top = gr.rect.top - (72 + gr.rect.height)
