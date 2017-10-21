import pygame,sys,Sound
import info as inf
from Button import Button
from pygame.locals import *
class Menu():
    def __init__(self):
        self.image = pygame.image.load("Images\BackGrounds\Menu.gif")
        self.image1 = pygame.image.load('Images\Kursors\Mn.png')
        self.logo = pygame.image.load("Images\BackGrounds\Logo.jpg")
        self.Button1 = Button('PLAY','Images/Tree/Tree.png')
        self.Button2 = Button('QUIT','Images/Tree/Tree.png')
        self.Button1.rect.left = (inf.screenwidth // 2) - (self.Button1.rect.width // 2)
        self.Button1.rect.top = (inf.screenheight // 2) - (self.Button1.rect.height // 2)
        self.Button2.rect.left = (inf.screenwidth // 2) - (self.Button2.rect.width // 2)
        self.Button2.rect.top = (inf.screenheight // 2) - (self.Button2.rect.height // 2) + 100
        self.Do = None
        self.FonSound = Sound.Sound('Sounds\MenuSound.ogg',-1,0.1)
        self.ButtonSound = Sound.Sound('Sounds\MenuButton.ogg',0,0.2)
    def menu(self,screen,mouse):
        done = True
        self.FonSound.playsound()
        screen.blit(self.logo,(0,0))
        pygame.display.update()
        pygame.time.wait(4500)
        while done:
            mouse.update()
            if pygame.sprite.collide_rect(mouse,self.Button1):
                self.ButtonSound.playsound()
                self.Do = 1
            elif pygame.sprite.collide_rect(mouse,self.Button2):
                self.Do = 2
                self.ButtonSound.playsound()
            else:
                self.Do = 0
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if self.Do == 1:
                        done = False
                        self.FonSound.stopsound()
                    if self.Do == 2:
                        sys.exit()
            screen.blit(self.image, (0,0))
            screen.blit(self.Button1.image,self.Button1.rect)
            screen.blit(self.Button2.image,self.Button2.rect)
            pygame.display.update()
