import pygame
import info as inf
import Sound
from pygame.locals import *
import random
class Player(pygame.sprite.Sprite):
    def __init__(self,openAnimation):
        super(Player,self).__init__()
        self.images = []
        self.imagesT = []
        self.Wimages = []
        self.WimagesT =[]
        openAnimation(self,'Player12',self.images,'.gif','Images/Player/',4)
        openAnimation(self,'Player12W',self.Wimages,'.gif','Images/Player/',6)
        openAnimation(self,'Player12T',self.imagesT,'.gif','Images/Player/',4)
        openAnimation(self,'Player12WT',self.WimagesT,'.gif','Images/Player/',6)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.left = inf.screenwidth // 2
        self.OG = False
        self.do = True
        self.index = 0
        self.speed = 0
        self.maxspeed = 16
        self.AnimSpeed = 3
        self.WalkAnimSpeed = 2
        self.Gravity = 6
        self.Health = inf.PlayerHealth
        self.alive = True
        self.defens = 0
        self.walksound = Sound.Sound('Sounds/Walk.ogg',0,0.1)
        self.jump = 0
        self.left = 683
        self.stay = True
        self.Leftside = True
        self.jumping = False
        self.maxjump = 30
        self.damagebonus = 0
        self.PlayerParametrs = [self.rect.top,self.rect.left,self.OG,self.index,self.speed,self.maxspeed,self.Health,self.alive,self.defens,self.jump,self.left,self.maxjump,self.damagebonus]
    def MouseLeftorRight(self,AnimPlay):
        print(self.damagebonus)
        x,y = pygame.mouse.get_pos()
        if self.rect.left + 16 > x:
            self.Leftside = True
            AnimPlay(self,self.imagesT,self.AnimSpeed)
        elif self.rect.left + 16 < x:
            self.Leftside = False
            AnimPlay(self,self.images,self.AnimSpeed)
    def data(self):
        self.rect.top,self.rect.left,self.OG,self.index,self.speed,self.maxspeed,self.Health,self.alive,self.defens,self.jump,self.left,self.maxjump,self.damagebonus = self.PlayerParametrs
    def dataupdate(self):
        self.PlayerParametrs = [self.rect.top,self.rect.left,self.OG,self.index,self.speed,self.maxspeed,self.Health,self.alive,self.defens,self.jump,self.left,self.maxjump,self.damagebonus]
    def update(self,pressed_keys,ground1,wall,AnimPlay,all_sprites,Plus,Minus,doors):
        if self.do == True:
            self.data()
            self.do = False
        self.dataupdate()
        if self.Health <= 0:
            self.alive = False
        if self.alive == True:
            for gr1 in ground1:
                rect = pygame.Rect(tuple(gr1),(inf.Ground_Block_Width,inf.Ground_Block_Height_For_Rect_Collide))
                if rect.colliderect(self.rect):
                    self.OG = True
                    break
                else:
                    self.OG = False
            for gt in ground1:
                rect1 = pygame.Rect(gt,(inf.Ground_Block_Width,inf.Ground_Block_Height_For_Rect_Collide))
                if self.rect.colliderect(rect1):
                    if gt[1] - self.rect.top <= self.rect.height - inf.Ground_Block_Height:
                        if self.rect.left > gt[0]:
                             if pressed_keys[K_LEFT]:
                                 self.rect.top -= 18
                                 AnimPlay(self,self.Wimages,self.AnimSpeed)
                                 self.walksound.playsound()
                             if pressed_keys[K_RIGHT]:
                                 AnimPlay(self,self.WimagesT,self.AnimSpeed)
                                 self.walksound.playsound()
                        elif self.rect.left < gt[0]:
                              if pressed_keys[K_RIGHT]:
                                  self.rect.top -= 18
                                  AnimPlay(self,self.WimagesT,self.AnimSpeed)
                                  self.walksound.playsound()
                              if pressed_keys[K_LEFT]:
                                  AnimPlay(self,self.Wimages,self.AnimSpeed)
                                  self.walksound.playsound()
            if pressed_keys[K_LEFT]:
                if not self.speed >= self.maxspeed:
                    self.speed += 1
                if self.stay == True:
                    self.speed = 1
                if inf.blithome == True:
                    if self.rect.left <= 0 + self.rect.width:
                        pass
                    else:
                        self.rect.left -= self.speed
                        self.left -= self.speed
                else:
                    self.rect.left -= self.speed
                    self.left -= self.speed
                AnimPlay(self,self.WimagesT,self.WalkAnimSpeed)
                if not inf.blithome == True:
                    Plus(all_sprites,self.speed,ground1)
                self.walksound.playsound()
                self.stay = False
                self.Leftside = True
            elif pressed_keys[K_RIGHT]:
                 if not self.speed >= self.maxspeed:
                     self.speed += 1
                 if self.stay == True:
                     self.speed = 1
                 if inf.blithome == True:
                     if self.rect.left >= inf.screenwidth - self.rect.width:
                         pass
                     else:
                         self.rect.left += self.speed
                         self.left += self.speed
                 else:
                     self.rect.left += self.speed
                     self.left += self.speed
                 AnimPlay(self,self.Wimages,self.WalkAnimSpeed)
                 if not inf.blithome == True:
                     Minus(all_sprites,self.speed,ground1)
                 self.stay = False
                 self.walksound.playsound()
                 self.Leftside = False
            else:
                self.stay = True
                self.MouseLeftorRight(AnimPlay)
            if pressed_keys[K_UP]:
                if self.OG == True:
                        self.jumping = True
            if self.jumping == True:
                if not self.jump >= self.maxjump:
                    self.jump += 9
                elif self.jump >= self.maxjump:
                    self.jump = 0
                    self.jumping = False
                self.rect.top -= self.jump
            if not self.OG == True:
                self.rect.top += self.Gravity
