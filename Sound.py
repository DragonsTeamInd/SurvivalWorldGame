import pygame
from pygame.locals import *
class Sound():
    def __init__(self,soundfile,playloops,vol):
        self.sound = pygame.mixer.Sound(soundfile)
        self.playloopsnum = playloops
        self.sound.set_volume(vol)
    def playsound(self):
        self.sound.play(self.playloopsnum)
    def stopsound(self):
        self.sound.stop()
