import pygame
from pygame.locals import *
from win32api import GetSystemMetrics
import random
#Frame Speed
FrameSpeedController = pygame.time.Clock()
#Resourses
WoodResourse = 0
WoolResourse = 0
#Is programm is running
Work = True
#Create the world(Every time you open a game it True)
Create_Field = True
#Ground Block ID
Created_Ground_Block_Number = 1
#Frame Speed
b = 1
#Inventory Sizes
Inventory_Width = 6
Inventory_Height = 3
#Sizes of screen
screenwidth = GetSystemMetrics(0)
screenheight = GetSystemMetrics(1)
#Size of Ground Blocks
Ground_Block_Width = 96
Ground_Block_First_Position = screenheight // 2
Ground_Block_Height = 16
Ground_Block_Height_For_Rect_Collide = 1920
Ground_Texture_Block_Height = 48
####Chanses for spwaning/creating
#Ground Chanse
chanse = 5
#Tree Chanse
TreeNChaseb = 0
TreeNChasef = 20
TreeChaseb = 0
TreeChasef = 100
TreeChase = 95
#Grass Chanse
GrassNChaseb = 0
GrassNChasef = 200
GrassChaseb = 0
GrassChasef = 100
GrassChase = 50
#Chanse of spawning(Will be deleted soon)
SChansbz = 1
SChansfz = 6
Zombierectwidth = 36
SSChansbz = 0
SSChansfz = 100
SSChansz = 20
#Player step(For camera)
OnePlayerStep_inPXL = 4
#World Size
WorldSizeInPXL = screenwidth * 2
#Using with "drawing" the screen
IsCraftWindowIsOpen = False
#Using for nonclassed objects
object = None
#Health
PlayerHealth = 100
#Armor ID in invenory
ArmorID = 0
#MeeleWeapon ID in invenory
MeeleWeaponID = 0
#XP/Expirence
PlayerExpirence = 0
#Is it day or night(True == Day,False == Night)
Day = True
#Using for "drawing" screen
blithome = False
#Power Up Point(Using for talants)
PowerUpPoints = 10000
#Create enemies(Every time you open a game it True)
CreateEnemy = True
