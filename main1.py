import pygame
import Armor as Arm
import Player as P
import Window as Win
import Events as Evnt
import Groups as Lts
import MainsFuncs as MaF
import Field as F
import Animation as Anim
import GroundBlock as GB
import info as inf
import Grass as G
import Menu as M
import inventory as Inv
import inventoryBlock as IB
import SpawnEnemy as SpwEnm
import CraftWindow as CW
import Cursour as CS
import HUD as H
import EquipedItemsSector as EIS
import PlayersSpawn
import QuestMaker as QM
import QuestList as QL
import QuestCompleteChecker as QCC
import QuestChr as QC
import Home as Hm
import Timer as Time
import Resourses as Rs
import Talants as Tls
import TalantsWindow as TlW
import DataSave_And_DataOpen as Txt
import ArmorDataSaver as AS
import Loading as LoD
from pygame.locals import *
import random
if __name__ == '__main__':
    pygame.mixer.init()
    MTls = Tls.Talants()
    MTlW = TlW.TalantsWindow()
    MQchr = QC.QuestChr()
    MTime = Time.Timer()
    MRS = Rs.Resourses()
    MQCC = QCC.QuestCompliteChecker()
    MQM = QM.QuestMaker()
    MQL = QL.QuestList()
    MPS = PlayersSpawn.PlayersSpawn()
    MFuncs = MaF.MainsFuncs()
    MAnim = Anim.Animation()
    MWindow = Win.Window()
    MCraft = CW.CraftWindow()
    ME = Evnt.Events()
    MGroups = Lts.Groups()
    MH = Hm.Home(MGroups.ground)
    MF = F.Field()
    MPlayer = P.Player(MAnim.openAnimation)
    MGroups.all_sprites.add(MPlayer)
    MMenu = M.Menu()
    MInv = Inv.Inventory()
    MMenu.menu(MWindow.screen)
    MF.SoundFon.playsound()
    MSpawner = SpwEnm.SpawnEnemy()
    MCursour = CS.Cursour()
    MHUD = H.HUD()
    MEIS = EIS.EquipedItemsSector()
    MLoading = LoD.Loading(MAnim.openAnimation)
    while inf.running:
        MWindow.Rendering(MGroups.all_sprites,MPlayer,MGroups.grs,MAnim.AnimPlay,MGroups.ground1)
        for event in pygame.event.get():
            if event.type == QUIT:
                print(MPlayer.alive)
                Txt.savedata(MPlayerParametrs,'PlayerParametrs.txt')
                AS.savearmor(MGroups.Armors)
                inf.running = False
            if MPlayer.alive == True:
                if event.type == pygame.MOUSEBUTTONUP:
                    for MeeleWeapon in MGroups.MeeleWeapon:
                        MeeleWeapon.Attak(MGroups.zombies,MPlayer)
                MTls.opentalant(MCursour,event)
                MInv.buttonupdate(event)
                MGroups.craftblocks.update(MCursour,MGroups,event,MWindow.screen,MRS.Resourses)
                pressed_keys = pygame.key.get_pressed()
                MGroups.zombies.update(MPlayer,MAnim.AnimPlay,MGroups.ground1,MWindow.screen,event,ME.bite,ME.closenumevent,'event',MGroups.ItemDropsG,MGroups.all_sprites)
                MCraft.cameraupdate(event,MGroups.craftblocks)
                MWindow.dayornight(event,ME.oneminute,MAnim.AnimPlay)
        if MPlayer.alive == True:
            pressed_keys = pygame.key.get_pressed()
            MTlW.update(MTls.talants,pressed_keys,MWindow.screen)
            MInv.update(MGroups.InvBlocks2,MWindow.screen)
            MPlayer.update(pressed_keys,MGroups.ground,MGroups.wall,MAnim.AnimPlay,MGroups.all_sprites,MF.Plus,MF.Minus,MGroups.doors)
            MRS.updateR()
            MRS.updateC()
            MInv.updateR(MRS.Resourses)
            MInv.updateArmor(MGroups.Armors)
            MInv.updateMeeleWeapon(MGroups.MeeleWeapon)
            MInv.MakeInv(MGroups.InvBlocks2,MGroups.Armors,MGroups.MeeleWeapon,MRS.Resourses)
            MEIS.EquipListBlit(MGroups.Armors,MWindow.screen,MGroups.MeeleWeapon)
            MH.updateall(MPlayer,MTime.update,MWindow.screen,pressed_keys,MGroups.ground1,MGroups.ground,MCursour,MQchr.updateAll)
            if inf.CG == True:
                MWindow.RenderingLoading(inf.CG)
                MAnim.ThreadPlay((MLoading.images,MLoading.speed,MWindow.screen))
                Txt.opendata('PlayerParametrs.txt',MPlayer.PlayerParametrs)
                AS.openarmor(MGroups.Armors,Arm.Armor)
                MCraft.CreateCraftWindow(MGroups.craftblocks,MGroups,MAnim.openAnimation)
                MF.CreateGround(MGroups.all_sprites,GB.GroundBlock,MGroups.ground,MGroups.ground1)
                MF.BuildTrees(MGroups.ground1,Tr.Trees,MGroups.treess,MGroups.all_sprites)
                MF.BuildGrass(MGroups.ground1,G.Grass,MGroups.all_sprites,MGroups.grs,MAnim.openAnimation)
                MPS.SpawnOnGround(MGroups.ground1,MPlayer)
                MQM.QuestCreate(MGroups.quests)
                MTls.CreateTalants()
                inf.CG = False
            MCursour.update()
            MTls.update(MPlayer)
            MInv.updatepressitems(MGroups.InvBlocks2,MWindow.screen,MGroups.Armors,pressed_keys)
            MInv.updatenumres(MGroups.InvBlocks2,MWindow.screen,MRS.Resourses)
            MSpawner.SpawnAll(MAnim.openAnimation,MGroups.all_sprites,MGroups.zombies,MGroups.ground1,MPlayer)
            MGroups.zombies.update(MPlayer,MAnim.AnimPlay,MGroups.ground1,MWindow.screen,None,ME.bite,ME.closenumevent,'notevent',MGroups.ItemDropsG,MGroups.all_sprites)
            MGroups.quests.update()
            MQCC.check(MGroups.quests,MGroups.Armors,MGroups.MeeleWeapon)
            MFuncs.GroupUpdate(MGroups.MeeleWeapon,(MPlayer,MGroups.all_sprites,MGroups.InvBlocks2,MAnim.AnimPlay,MWindow.screen))
            MFuncs.GroupUpdate(MGroups.Armors,(MPlayer,MGroups.all_sprites,MGroups.InvBlocks2,MWindow.screen,MGroups.Armors))
            MFuncs.GroupUpdate(MGroups.ItemDropsG,(MGroups.ground1,MPlayer,MWindow.screen))
            MF.RenderGround(MGroups.all_sprites,MGroups.ground,MGroups.ground1,GB.GroundBlock,MPlayer,MGroups.treess,Tr.Trees,MGroups.grs,G.Grass,MAnim.openAnimation)
            MCraft.render(MGroups.craftblocks,pressed_keys,MWindow.screen)
            MQL.update(pressed_keys,MWindow.screen,MGroups.quests)
            MHUD.update(MPlayer,MWindow.screen)
            pygame.display.flip()
            inf.fpsclock.tick(10000)
