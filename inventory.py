import pygame
import info as inf
import inventoryBlock as invb
from pygame import *
class Inventory():
    def __init__(self):
        self.size = [['-'] * inf.Inventory_Width for i in range(inf.Inventory_Height)]
        self.sizecopy = [['-'] * inf.Inventory_Width for i in range(inf.Inventory_Height)]
        self.buttonimage = pygame.image.load('Images/Inventory/chest.gif')
        self.EQPblItems = []
        self.open = False
    def updateR(self,Resourses):
        for R in Resourses:
            if R.ininventory == True:
                b = 0
                for i in self.size:
                    a = 0
                    if R.ininventory == False:
                        break
                    for q in i:
                        if q == '-' or q == '-F':
                            self.sizecopy[b][a] = R.type
                            R.ininventory = False
                            a += 1
                            break
                    b += 1
            self.size = self.sizecopy
    def updateArmor(self,Armors):
        if len(Armors) > 0:
            for Ae in Armors:
                b = 0
                for i in self.size:
                    for q in i:
                        if Ae.ininventory == True:
                            if q == '-' or q == '-F':
                                if Ae.addicoininventory == True:
                                    self.sizecopy[b][i.index(q)] = '-A'
                                    Ae.addicoininventory = False
                    b += 1
        self.size = self.sizecopy
    def updateMeeleWeapon(self,MeeleWeapon):
        if len(MeeleWeapon) > 0:
            for MW in MeeleWeapon:
                b = 0
                for i in self.size:
                    for q in i:
                        if MW.ininventory == True:
                            if q == '-' or q == '-F':
                                if MW.addicoininventory == True:
                                    self.sizecopy[b][i.index(q)] = '-MW'
                                    MW.addicoininventory = False
                    b += 1
        self.size = self.sizecopy
    def InventoryBlockMaker(self,image,stroka,stolb,invblocks,type,strokam,Btype,object):
        new_invblock = invb.InventoryBlock(Btype)
        if not image == None:
            new_invblock.image = image
        new_invblock.rect.top = stroka * new_invblock.rect.height
        new_invblock.rect.left = stolb * new_invblock.rect.width
        new_invblock.item = object
        invblocks.append(new_invblock)
        if not stolb > len(strokam) - 1 or stroka > len(self.size) - 1:
            self.sizecopy[stroka][stolb] = type
        self.size = self.sizecopy
    def MakeNone(self,stolbm,stolb,stroka,invblocks,strokam):
        if stolbm == '-':
            self.InventoryBlockMaker(None,stroka,stolb,invblocks,'-F',strokam,'None',None)
            stolb += 1
        elif stolbm == '-F':
            stolb += 1
    def MakeRes(self,stolbm,stolb,stroka,invblocks,strokam,Resourses):
        for R in Resourses:
            if stolbm == R.type:
                self.InventoryBlockMaker(R.invimage,stroka,stolb,invblocks,R.type + 'F',strokam,R.Rtype,'Resours')
                stolb += 1
            elif stolbm == R.type + 'F':
                stolb += 1
    def MakeArmor(self,stolbm,stolb,stroka,invblocks,Armors,strokam):
        if len(Armors) > 0:
            if stolbm == '-A':
                for Armor in Armors:
                    if Armor.ininventory == True and Armor.icoininventory == True:
                        inf.ArmorID += 1
                        self.InventoryBlockMaker(Armor.ico,stroka,stolb,invblocks,'-FA' + str(inf.ArmorID),strokam,'EquipblItem',Armor)
                        Armor.icoininventory = False
                        Armor.id = inf.ArmorID
                        stolb += 1
                        break
            for Armor in Armors:
                if not Armor.id == None:
                    if stolbm == '-FA' + str(Armor.id):
                        if Armor.equpe == True and Armor.candelete == True:
                            if not stolb > len(strokam) - 1 or stroka > len(self.size) - 1:
                                self.sizecopy[stroka][stolb] = '-'
                                Armor.candelete = False
                                break
                        stolb += 1
            self.size = self.sizecopy
    def MakeMeeleWepaon(self,stolbm,stolb,stroka,invblocks,MeeleWeapon,strokam):
        if len(MeeleWeapon) > 0:
            if stolbm == '-MW':
                for MW in MeeleWeapon:
                    if MW.ininventory == True and MW.icoininventory == True:
                        inf.MeeleWeaponID += 1
                        self.InventoryBlockMaker(MW.ico,stroka,stolb,invblocks,'-FMW' + str(inf.MeeleWeaponID),strokam,'EquipblItem',MW)
                        MW.icoininventory = False
                        MW.id = inf.MeeleWeaponID
                        stolb += 1
                        break
            for MW in MeeleWeapon:
                if not MW.id == None:
                    if stolbm == '-FMW' + str(MW.id):
                        if MW.equpe == True and MW.candelete == True:
                            if not stolb > len(strokam) - 1 or stroka > len(self.size) - 1:
                                self.sizecopy[stroka][stolb] = '-'
                                MW.candelete = False
                                break
                        stolb += 1
            self.size = self.sizecopy
    def MakeInv(self,invblocks,Armors,MeeleWeapon,Resourses):
        stroka = 0
        for strokam in self.size:
            stolb = 0
            for stolbm in strokam:
                self.MakeNone(stolbm,stolb,stroka,invblocks,strokam)
                self.MakeRes(stolbm,stolb,stroka,invblocks,strokam,Resourses)
                self.MakeArmor(stolbm,stolb,stroka,invblocks,Armors,strokam)
                self.MakeMeeleWepaon(stolbm,stolb,stroka,invblocks,MeeleWeapon,strokam)
                stolb += 1
            stroka += 1
    def deleteivnblocks(self,invblock):
        if len(invblock) > inf.Inventory_Width * inf.Inventory_Height:
            for block in invblock:
                block.kill()
                break
    def update(self,invblock,screen):
        if self.open == False:
            screen.blit(self.buttonimage,(0,0))
        elif self.open == True:
            for block in invblock:
                screen.blit(block.image,block.rect)
            screen.blit(self.buttonimage,(36*inf.InventoryW,0))
        self.deleteivnblocks(invblock)
    def buttonupdate(self,event):
        x,y = pygame.mouse.get_pos()
        if self.open == False:
            if x > 0 and x < 0 + 36 and y > 0 and y < 0 + 36:
                if event.type == MOUSEBUTTONUP:
                    self.open = True
        if self.open == True:
            if x > inf.InventoryW*36 and x < inf.InventoryW*36 + 36 and y > 0 and y < 0 + 36:
                if event.type == MOUSEBUTTONUP:
                    self.open = False
    def Text(self,TxT,font,size):
        Text = TxT
        TextFont = pygame.font.SysFont(font, size)
        TextFontImage = TextFont.render(Text, 0, (255,255,255))
        return TextFontImage
    def blockequpeControll(self,block,EQnumtype):
        if EQnumtype > 1:
            if block.item.equpe == True:
                block.type = 'EquipblItem'
                block.item.equpe = False
                block.item.icoininventory = True
                block.item.addicoininventory = True
                block.item.candelete = True
                EQnumtype -= 1
            else:
                block.item.equpe = True
        else:
            block.item.equpe = True
    def ItemsControll(self,invblock):
        EQArmor = 0
        EQMeeleWeapon = 0
        for block in invblock:
            if block.type == 'EquipedItemArmor':
                EQArmor += 1
                self.EQPblItems.append(block)
            if block.type == 'EquipedItemMeeleWeapon':
                EQMeeleWeapon += 1
                self.EQPblItems.append(block)
        for block in self.EQPblItems:
            self.blockequpeControll(block,EQArmor)
            self.blockequpeControll(block,EQMeeleWeapon)
        self.EQPblItems.clear()
    def TextBlit(self,x,y,screen,Image,block,Equip,k,invblock):
        if x > block.rect.left and x < block.rect.left + block.rect.width and y > block.rect.top and y < block.rect.top + block.rect.height:
            screen.blit(Image,(x,y - 20))
            if Equip == True:
                if k:
                    block.type = block.item.type
                    self.ItemsControll(invblock)
    def updatenumres(self,invblocks,screen,Resourses):
        if self.open == True:
            for R in Resourses:
                x,y = pygame.mouse.get_pos()
                for block in invblocks:
                    Image = self.Text(str(R.count),"None",20)
                    if block.type == R.Rtype:
                        self.TextBlit(x,y,screen,Image,block,False,None,invblocks)
    def updatepressitems(self,invblocks,screen,Armors,pk):
        if self.open == True:
            for block in invblocks:
                if block.type == 'EquipblItem':
                    TImage = self.Text('Press "Q" to equip',"None",20)
                    x,y = pygame.mouse.get_pos()
                    self.TextBlit(x,y,screen,TImage,block,True,pk[K_q],invblocks)
