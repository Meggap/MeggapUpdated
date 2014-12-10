'''
Created on 15/09/2014

@author: rodrigo
'''

import pygame
import constantes
import platforms
import platforms2
from levels import Level

# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("imagenes/fondonivel2.png").convert()
        self.level_limit = -35000

        # Array with type of platform, and x, y location of the platform.
        level = [ 
                 [platforms.PISO, -150, 490],
                 [platforms.PISO, 4500, 490],
                 [platforms.PISO, 10050, 490],
                 [platforms.PISO, 16050, 490],
                 [platforms.PISO, 22050, 490],
                 [platforms.PISO, 28050, 490],
                 [platforms.PISO, 34050, 490]
                  
                  ]
           # Go through the array above and add platforms


        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            
            
            
            
            
            
        level = [ 
                 [platforms2.TORRE, 500, 420],
                 [platforms2.BASICO1, 700, 350],
                 [platforms2.LARGO1, 900, 400],
                 [platforms2.MEDIANO1, 1000, 400],

                  
                  ]
                         
            
        for platform in level:
            block = platforms2.Platform2(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            

        level = [ [platforms.PISO, 100, 0]

                  ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.VerticalPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
            
            
            
            
        # Add a custom moving platform
        #block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        #block.rect.x = 1500
        #block.rect.y = 300
        #block.boundary_top = 100
        #block.boundary_bottom = 550
        #block.mover_y = -1
        #block.player = self.player
        #block.nivel = self
        #self.platform_list.add(block)