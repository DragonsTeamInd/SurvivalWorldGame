import pygame
import info as inf
from pygame.locals import *
import random
class Window():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((inf.screenwidth,inf.screenheight),FULLSCREEN)
        self.imagesDoN = []
        self.imagesDoN.append(pygame.image.load("Images/Backgrounds/Day.png").convert_alpha())
        self.imagesDoN.append(pygame.image.load("Images/Backgrounds/Night2.png").convert_alpha())
        self.image = self.imagesDoN[0]
        self.bck = pygame.image.load("Images\Backgrounds\BG2.png")
        self.Gen = pygame.image.load("Images\Backgrounds\Gen.png")
        self.imageb = pygame.image.load('Images\Ground\GroundPillow.png')
        self.dead = pygame.image.load("Images\Backgrounds\Dead.png").convert_alpha()
        self.index = 0
        self.bck = pygame.transform.scale(self.bck,(inf.screenwidth,inf.screenheight))
        self.Gen = pygame.transform.scale(self.Gen,(inf.screenwidth,inf.screenheight))
        self.dead = pygame.transform.scale(self.dead,(inf.screenwidth,inf.screenheight))
        self.imagesDoN[0] = pygame.transform.scale(self.imagesDoN[0],(inf.screenwidth,inf.screenheight))
        self.imagesDoN[1] =pygame.transform.scale(self.imagesDoN[1],(inf.screenwidth,inf.screenheight))
    def Rendering(self,all_sprites,player,grs,AnimPlay,gr1):
        if player.alive == True:
            if inf.IsCraftWindowIsOpen == False:
                if not inf.blithome == True:
                    self.screen.blit(self.bck,[0,0])
                    for i in gr1:
                        self.screen.blit(self.imageb,i)
                    for i in grs:
                        i.update(AnimPlay)
                    for en in all_sprites:
                        if en.rect.left > player.rect.left:
                            if en.rect.left - player.rect.left <= inf.screenwidth // 2 + 100:
                                self.screen.blit(en.image, en.rect)
                        else:
                            if player.rect.left - en.rect.left <= inf.screenwidth // 2 + 100:
                                self.screen.blit(en.image, en.rect)
                    self.screen.blit(self.image,(0,0))
                else:
                    self.screen.blit(self.bck,[0,0])
        else:
            self.screen.blit(self.dead,(0,0))
            pygame.display.flip()
    def RenderingLoading(self,CG):
        if CG == True:
            self.screen.blit(self.Gen,[0,0])
            pygame.display.flip()
    def dayornight(self,event,oneminute,AnimPlay):
        if event.type == oneminute:
            AnimPlay(self,self.imagesDoN,1)
        if self.image == self.imagesDoN[1]:
            inf.Day = False
        else:
            inf.Day = True
        print(inf.Day)
