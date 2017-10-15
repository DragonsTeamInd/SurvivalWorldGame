import pygame
import info as inf
from pygame.locals import *
import random
import threading
class Animation():
    def openAnimation(self,slf,Img,images,rsr,folder,rng):
        for i in range(rng):
            if i == 0:
                images.append(pygame.image.load(folder + Img + rsr))
            else:
                images.append(pygame.image.load(folder + Img + str(i) + rsr))
            images[i].set_colorkey((255,255,255))
    def AnimPlay(self,slf,images,speed):
        slf.index += 1
        if slf.index >= len(images) * speed:
            slf.index = 0
        slf.image = images[slf.index // speed]
    def LoadingPlay(self,images,speed,screen):
        index = 0
        while inf.Create_Field == True:
            index += 1
            if index >= len(images) * speed:
                index = 0
            image = images[index // speed]
            screen.blit(image,((inf.screenwidth // 2) - (image.get_rect().width // 2),(inf.screenheight // 2) - (image.get_rect().height // 2)))
            pygame.display.flip()
    def ThreadPlay(self,argss):
        thread = threading.Thread(target = self.LoadingPlay,args = argss)
        thread.start()
