import pygame
from pygame import *
from BasicObj import BasicObj
import info as inf
from GroundBlock import GroundBlock
class Home():
    def __init__(self,ground):
        self.groundobj = GroundBlock()
        self.ground = pygame.image.load('images/Ground/HomesGround.png')
        self.groundobj.image = self.ground
        self.groundobj.rect = self.ground.get_rect()
        self.groundobj.rect.top = inf.screenheight // 2
        self.openstyle = False
        self.houseopen = pygame.image.load('images/Try List/OH.png')
        self.houseclose = pygame.image.load('images/Try List/CH.png')
        self.open = False
        self.buttonpressed = False
    def BlitHome(self,screen,player):
        inf.blithome = True
        screen.blit(self.ground,(0,inf.screenheight // 2))
        if self.openstyle == True:
            screen.blit(self.houseopen,((inf.screenwidth // 2) - (self.houseopen.get_rect().width // 2),(inf.screenheight // 2) - (self.houseopen.get_rect().height)))
        elif self.openstyle == False:
            screen.blit(self.houseclose,((inf.screenwidth // 2) - (self.houseopen.get_rect().width // 2),(inf.screenheight // 2) - (self.houseopen.get_rect().height)))
        screen.blit(player.image,player.rect)
    def collide_check(self,player):
        image = pygame.Surface((self.houseopen.get_rect().width,self.houseopen.get_rect().height))
        rectl = (inf.screenwidth // 2) - (image.get_rect().width // 2)
        rectt = (inf.screenheight // 2) - (image.get_rect().height)
        Home = BasicObj(image,0)
        Home.rect.left = rectl
        Home.rect.top = rectt
        if pygame.sprite.collide_rect(Home,player):
            self.openstyle = True
        else:
            self.openstyle = False
    def update(self,screen,ground1,player):
        if self.open == True:
            self.BlitHome(screen,player)
        else:
            inf.blithome = False
    def teleport(self,ground1,ground):
        if self.open == False:
            self.open = True
            for i in ground1:
                ground.remove(i)
            ground.add(self.groundobj)
        else:
            self.open = False
            for i in ground1:
                ground.add(i)
            ground.remove(self.groundobj)
        self.buttonpressed = False
    def buttonupdate(self,pk):
        if pk[K_h]:
            self.buttonpressed = True
    def TimeUpdate(self,Tupdate,player,ground1,ground):
        if self.buttonpressed == True:
            Tupdate(5,self.teleport,(ground1,ground))
            player.rect.top -= 50
    def updateall(self,player,Tupdate,screen,pk,ground1,ground,mouse,updateAll):
        self.collide_check(player)
        self.buttonupdate(pk)
        self.TimeUpdate(Tupdate,player,ground1,ground)
        self.update(screen,ground1,player)
        if inf.blithome == True:
            updateAll(mouse,player,screen)
