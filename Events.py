import pygame
from pygame import *
class Events():
    def __init__(self):
        self.bite = pygame.USEREVENT + 1
        pygame.time.set_timer(self.bite, 1500)
        self.closenumevent = pygame.USEREVENT + 2
        pygame.time.set_timer(self.closenumevent, 1500)
        self.oneminute = pygame.USEREVENT + 3
        pygame.time.set_timer(self.oneminute, 180000)
    def eventcreate(self,time):
        event = pygame.USEREVENT + 1
        pygame.time.set_timer(event, time)
        return event
