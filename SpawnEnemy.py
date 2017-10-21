import pygame
import info as inf
import Enemy as ez
from pygame.locals import *
import random
class SpawnEnemy():
    def __init__(self):
        self.EnemyList = []
        self.EnemyList.append('Zombie')
    def SpawnAll(self,openAnimation,all_sprites,zombies,ground1,player):
        if inf.CreateEnemy == True:
            for EnemyType in self.EnemyList:
                if EnemyType == 'Zombie':
                    Chans = random.randint(inf.SChansbz,inf.SChansfz)
                    for place in ground1:
                            Chans = random.randint(inf.SChansbz,inf.SChansfz)
                            if random.randint(inf.SSChansbz,inf.SSChansfz) <= inf.SSChansz:
                                new_zombie = ez.Enemy(openAnimation,'EnemyST','.gif','Images/Enemy[Zombie]/',100,3,4,20,3,5,20,30,[pygame.image.load('Images/Resourses/wool.png').convert_alpha()])
                                new_zombie.rect.left = place[0]
                                for gr in ground1:
                                    if new_zombie.rect.left - gr[0] <= inf.Ground_Block_Width and new_zombie.rect.left - gr[0] > 0:
                                        new_zombie.rect.top = gr[1] - new_zombie.rect.height
                                        break
                                    if new_zombie.rect.left - gr[0] >= -inf.Ground_Block_Width and new_zombie.rect.left - gr[0] < 0:
                                        new_zombie.rect.top = gr[1] - new_zombie.rect.height
                                        break
                                all_sprites.add(new_zombie)
                                zombies.add(new_zombie)
            inf.CreateEnemy = False
