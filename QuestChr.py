import pygame
import random
from pygame import *
class QuestChr(pygame.sprite.Sprite):
    def __init__(self):
        super(QuestChr,self).__init__()
        self.image = pygame.image.load('images/QuestChar/quester.gif')
        self.SBaloon = pygame.Surface((100,20))
        self.rect = self.image.get_rect()
        self.rect.left = 60
        self.rect.top = 384 - self.rect.height
        self.speakedTxt = ''
        self.text = 'mainstory'
        self.usual_text = ['Hello!','Greatings','Thanks for helping!']
        self.blit_text = True
        self.ip = 0
        self.touched = False
        self.event = pygame.USEREVENT + 1
        self.MainHistorySpeaked = False
        pygame.time.set_timer(self.event, 5000)
    def SpeakBliOnScreen(self,screen):
        if self.blit_text == True:
            screen.blit(self.SBaloon,(self.rect.left + 20,self.rect.top + 20))
            Text = self.speakedTxt
            TextFont = pygame.font.SysFont('Font.otf', 30)
            T = TextFont.render(Text, 0, (255,255,255))
            screen.blit(T,(self.rect.left + 20,self.rect.top + 20))
    def update(self,mouse,player):
        if pygame.sprite.collide_rect(mouse,self):
            self.blit_text = True
            if self.touched == False:
                self.speakedTxt = random.choice(self.usual_text)
                self.touched = True
        else:
            self.blit_text = False
            self.touched = False
    def updateAll(self,mouse,player,screen):
        screen.blit(self.image,self.rect)
        self.update(mouse,player)
        self.SpeakBliOnScreen(screen)
