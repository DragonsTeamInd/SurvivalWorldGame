import pygame,sys,Sound
import info as inf
from pygame.locals import *
class Menu():
    def __init__(self):
        self.image = pygame.image.load("Images\BackGrounds\Menu.gif")
        self.image1 = pygame.image.load('Images\Kursors\Mn.png')
        self.logo = pygame.image.load("Images\BackGrounds\Logo.jpg")
        self.image1.set_colorkey((255,255,255))
        self.rect = self.image1.get_rect()
        self.rect.left = inf.MenuButtonCursorleft
        self.rect.top = inf.MenuButtonCursortop
        self.Do = None
        self.FonSound = Sound.Sound('Sounds\MenuSound.ogg',-1,0.1)
        self.ButtonSound = Sound.Sound('Sounds\MenuButton.ogg',0,0.2)
    def render(self):
        if self.Do == 1:
            self.rect.top = 300
        elif self.Do == 2:
            self.rect.top = 500
    def menu(self,screen):
        done = True
        self.FonSound.playsound()
        screen.blit(self.logo,(0,0))
        pygame.display.update()
        pygame.time.wait(2000)
        while done:
            x,y = pygame.mouse.get_pos()
            if x > inf.Button1left and x <inf.Button1left + inf.Button1width and y > inf.Button1top and y < inf.Button1top + inf.Button1height:
                if self.Do == 2:
                    self.Do = 1
                    self.ButtonSound.playsound()
                else:
                    self.Do = 1
            elif x > inf.Button2left and x < inf.Button2left + inf.Button2width and y > inf.Button2top and y < inf.Button2top + inf.Button2height:
                if self.Do == 1:
                    self.Do = 2
                    self.ButtonSound.playsound()
                else:
                    self.Do = 2
            self.render()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if self.Do == 1:
                        done = False
                        self.FonSound.stopsound()
                    if self.Do == 2:
                        sys.exit()
            screen.blit(self.image, (0,0))
            screen.blit(self.image1, self.rect)
            pygame.display.update()
