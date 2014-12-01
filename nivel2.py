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

        self.background = pygame.image.load("imagenes/fondolvl2.png").convert()
        self.level_limit = -35000

        # Array with type of platform, and x, y location of the platform.
        level = [ 
                 [platforms.PISO, 0, 490]
                  
                  
                  
                  ]


        #Artefactos
        #botellas = pygame.image.load("imagenes/botellas.png").convert()
        #botellas.set_colorkey(constantes.BLANCO)
        #borracho = pygame.image.load("imagenes/borracho.png").convert()
        #borracho.set_colorkey(constantes.BLANCO)
        #farol = pygame.image.load("imagenes/farol.png").convert()
        #farol.set_colorkey(constantes.BLANCO)
        #self.background.blit(botellas, (700, 550))
        #self.background.blit(borracho, (800, 450))
        #self.background.blit(farol, (1000, 460))

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