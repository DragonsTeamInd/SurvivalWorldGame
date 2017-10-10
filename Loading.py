import pygame
from pygame import *
class Loading():
    def __init__(self,openAnimation):
        self.images = []
        self.speed = 1
        openAnimation(1,'00',self.images,'.png','images/Loading/',20)
