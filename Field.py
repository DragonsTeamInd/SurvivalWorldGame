import pygame
import Sound
import info as inf
from pygame.locals import *
import random
class Field():
    def __init__(self):
        self.JFE = 0
        self.Q = 50
        self.QMax = 100
        self.SoundFon = Sound.Sound('Sounds\FonMusic223.ogg',-1,0.06)
        self.rect = 1
        self.rect1 = 1
    def RandomBlockY(self):
        Ground_Block_First_Position = inf.Ground_Block_First_Position
        if not self.Q == self.QMax and not self.Q == 0:
            if random.randint(0,100) >= 60:
                if random.randint(0,100) < self.Q:
                      self.JFE += inf.Ground_Block_Height
                      self.Q += inf.chanse
                      Ground_Block_First_Position += self.JFE
                else:
                      self.JFE -= inf.Ground_Block_Height
                      self.Q -= inf.chanse
                      Ground_Block_First_Position += self.JFE
            else:
                Ground_Block_First_Position += self.JFE
        else:
            self.Q = 50
            Ground_Block_First_Position += self.JFE
        return Ground_Block_First_Position
    def CreateGround(self,als,GroundBlock,gr,AllGroundRects):
        for i in range(inf.WorldSizeInPXL // inf.Ground_Block_Width + 1):
            new_rect = []
            new_rect.append(inf.Ground_Block_Width * inf.Created_Ground_Block_Number)
            new_rect.append(self.RandomBlockY())
            AllGroundRects.append(new_rect)
            inf.Created_Ground_Block_Number += 1
    def BuildTrees(self,AllGroundRects,Trees,treess,all_sprites):
        a = random.randint(inf.TreeNChaseb , inf.TreeNChasef)
        c = 0
        for i in AllGroundRects:
            if a > 0 and c == 40:
                if random.randint(inf.TreeChaseb , inf.TreeChasef) >= inf.TreeChase:
                    new_tree = Trees()
                    new_tree.rect.left = i[0] - new_tree.rect.width // 2
                    new_tree.rect.top = i[1] - new_tree.rect.height
                    treess.add(new_tree)
                    all_sprites.add(new_tree)
                    a -= 1
                    c = 0
            else:
                c += 5
    def BuildGrass(self,AllGroundRects,Grass,al,grs,openAnimation):
        a = random.randint(inf.GrassNChaseb , inf.GrassNChasef)
        for i in AllGroundRects:
                if a > 0:
                    if random.randint(inf.GrassChaseb , inf.GrassChasef) >= inf.GrassChase:
                        new_grass = Grass(openAnimation)
                        new_grass.rect.left = i[0]
                        new_grass.rect.top = i[1]
                        al.add(new_grass)
                        grs.add(new_grass)
                        a -= 1
    def RenderGrass(self,al,grs,gr1,Grass,openAnimation):
        for Grs in grs:
            Grs.kill()
        self.BuildGrass(gr1,Grass,al,grs,openAnimation)
    def RenderTrees(self,all_sprites,treess,gr1,Trees):
        for Trs in treess:
            Trs.kill()
        self.BuildTrees(gr1,Trees,treess,all_sprites)
    def RenderAll(self,all_sprites,treess,gr1,Trees,grs,Grass,openAnimation):
        self.RenderTrees(all_sprites,treess,gr1,Trees)
        self.RenderGrass(all_sprites,grs,gr1,Grass,openAnimation)
    def RenderGround(self,all_sprites,ground,gr1,GroundBlock,player,treess,Trees,grs,Grass,openAnimation):
        '''print(player.left)
        if player.left < (inf.screenwidth * 2 - (inf.screenwidth * 2) // 3) * (self.rect - 1):
            inf.Created_Ground_Block_Number -= (inf.screenwidth * 2 // inf.Ground_Block_Width + 1) * 1.5
            self.rect -= 1
            for gr in gr1:
                gr.kill()
            print('Malenko')
            self.JFE = 0
            inf.CreateEnemy = True
            player.rect.move_ip(0,-200)
            self.CreateGround(all_sprites,GroundBlock,ground,gr1)
            self.RenderAll(all_sprites,treess,gr1,Trees,grs,Grass,openAnimation)
        elif player.left > (inf.screenwidth * 2 - (inf.screenwidth * 2) // 3) * self.rect:
            self.rect += 1
            inf.Created_Ground_Block_Number -= ((inf.screenwidth * 2 - inf.screenwidth // 30) // inf.Ground_Block_Width + 1)
            for gr in gr1:
                gr.kill()
            print('Mnogo')
            self.JFE = 0
            inf.CreateEnemy = True
            player.rect.move_ip(0,-200)
            self.CreateGround(all_sprites,GroundBlock,ground,gr1)
            self.RenderAll(all_sprites,treess,gr1,Trees,grs,Grass,openAnimation)'''
    def Plus(self,all_sprites,OnePlayerStep_inPXL,AllGroundRects):
        for i in all_sprites:
            i.rect.left += OnePlayerStep_inPXL
        for j in AllGroundRects:
            j[0] += OnePlayerStep_inPXL
    def Minus(self,all_sprites,OnePlayerStep_inPXL,AllGroundRects):
        for i in all_sprites:
            i.rect.left -= OnePlayerStep_inPXL
        for j in AllGroundRects:
            j[0] -= OnePlayerStep_inPXL
