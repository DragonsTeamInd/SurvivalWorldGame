import pygame
from pygame.locals import *
class Groups():
    def __init__(self):
      self.all_sprites = pygame.sprite.Group()
      self.stoneG = pygame.sprite.Group()
      self.doors = []
      self.doors1 = pygame.sprite.Group()
      self.ground = pygame.sprite.Group()
      self.ground1 = pygame.sprite.Group()
      self.wall = []
      self.wall1 = pygame.sprite.Group()
      self.treess = pygame.sprite.Group()
      self.grs = pygame.sprite.Group()
      self.InvBlocks2 = []
      self.zombies = pygame.sprite.Group()
      self.TreeParts = pygame.sprite.Group()
      self.craftblocks = pygame.sprite.Group()
      self.Armors = []
      self.MeeleWeapon = []
      self.ItemDropsG = pygame.sprite.Group()
      self.quests = pygame.sprite.Group()
