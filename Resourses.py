import pygame
from pygame import *
from Resours import Resours
import info as inf
class Resourses():
    def __init__(self):
        self.Resourses = []
        self.woodis = False
    def updateC(self):
        if inf.woods > 0 and self.woodis == False:
            new_resourse = Resours('-W',inf.woods,'','WoodItem','wood')
            self.Resourses.append(new_resourse)
            self.woodis = True
    def updateR(self):
        for Resours in self.Resourses:
            if Resours.type == '-W':
                inf.woods = Resours.count
