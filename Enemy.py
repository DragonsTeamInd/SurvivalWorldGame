import pygame
import random
from pygame.locals import *
import random
from ItemDrop import ItemDrop
import info as inf
class Enemy(pygame.sprite.Sprite):
    def __init__(self,openAnimation,EnemyST,csr,pt,ad,spd,Aspd,health,damagemin,damagemax,Expirencemin,Expirencemax,items):
        super(Enemy,self).__init__()
        self.images = []
        openAnimation(self,EnemyST,self.images,csr,pt,5)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.AttakDistanse = ad
        self.items = items
        self.index = 0
        self.speed = spd
        self.AnimSpeed = Aspd
        self.health = health
        self.damagemin = damagemin
        self.damagemax = damagemax
        self.Expirencemin = Expirencemin
        self.Expirencemax = Expirencemax
        self.Gravity = 5
        self.OG = False
        self.damage = random.randint(self.damagemin,self.damagemax)
        self.blood = pygame.image.load('Images/Damge/Blood.png').convert_alpha()
    def ItemDrops(self,Group,all_sprites):
        image = random.choice(self.items)
        item = ItemDrop(image,self.items.index(image))
        Group.add(item)
        all_sprites.add(item)
        item.rect.left = self.rect.left
        item.rect.top = self.rect.top
    def update(self,player,AnimPlay,ground1,screen,event,bite,closenumevent,type,ItemDropsG,all_sprites):
        if type == 'notevent':
            if self.health == 0:
                self.ItemDrops(ItemDropsG,all_sprites)
                Expirence = random.randint(self.Expirencemin,self.Expirencemax)
                inf.PlayerExpirence += Expirence
                self.kill()
            a = player.rect.left - self.rect.left
            b = self.rect.left - player.rect.left
            for i in ground1:
                rect = pygame.Rect(tuple(i),(inf.Ground_Block_Width,inf.Ground_Block_Height))
                if self.rect.colliderect(rect):
                    self.OG = True
                else:
                    self.OG = False
                if self.rect.colliderect(rect):
                    if i[1] - self.rect.top <= 32:
                        if self.rect.left > i[0]:
                            if a > 0 and a <= self.AttakDistanse:
                                pass
                            elif b > 0 and b <= self.AttakDistanse:
                                if not pygame.sprite.collide_rect(self,player):
                                    self.rect.move_ip(0, -16)
                        elif self.rect.left < i[0]:
                              if a > 0 and a <= self.AttakDistanse:
                                  if not pygame.sprite.collide_rect(self,player):
                                      self.rect.move_ip(0, -16)
                              elif b > 0 and b <= self.AttakDistanse:
                                  if not pygame.sprite.collide_rect(self,player):
                                      pass
            if a > 0 and a <= self.AttakDistanse:
                if not pygame.sprite.collide_rect(self,player):
                    self.rect.move_ip(self.speed, 0)
            elif b > 0 and b <= self.AttakDistanse:
                if not pygame.sprite.collide_rect(self,player):
                    self.rect.move_ip(-self.speed, 0)
            else:
                AnimPlay(self,self.images,self.AnimSpeed)
            if not self.OG == True:
                self.rect.move_ip(0,self.Gravity)
            if self.rect.left - player.rect.left > inf.screenwidth // 2 + 36 or player.rect.left - self.rect.left > inf.screenwidth // 2 + 36:
                self.kill()
        if type == 'event':
                if event.type == bite and pygame.sprite.collide_rect(self,player):
                    print('e')
                    self.damage = random.randint(self.damagemin,self.damagemax)
                    attak = self.damage - player.defens
                    if attak >= 0:
                        player.Health -= attak
                if event.type == closenumevent and player.Health > 0 and pygame.sprite.collide_rect(self,player):
                     print('u')
                     screen.blit(self.blood,(0,0))
