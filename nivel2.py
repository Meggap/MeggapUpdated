'''
Created on 15/09/2014

@author: rodrigo
'''

import pygame
import constantes
import platforms
from levels import Level

# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("imagenes/background_02.png").convert()
        self.background.set_colorkey(constantes.BLANCO)
        self.level_limit = -1000

        # Array with type of platform, and x, y location of the platform.
        level = [  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
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