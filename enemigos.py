"""
Module for managing platforms.
"""
import pygame

from funciones_spritesheet import *
import jugador
from jugador import Player


class Enemigo(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    jugador_frame_izq = []
    jugador_frame_der = []
    

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheetNotas("imagenes/rastasht.png")
            
        #Recorte
        image = sprite_sheet.get_image(0, 0, 46, 81)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(46, 0, 46, 81)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(92, 0, 46, 81)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(138, 0, 46, 81)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(183, 0, 45, 81)
        self.jugador_frame_der.append(image)
        
        #Rotacion 
        image = sprite_sheet.get_image(0, 0, 46, 81)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(46, 0, 46, 81)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(92, 0, 46, 81)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(138, 0, 46, 81)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(183, 0, 45, 81)

        self.jugador_frame_izq.append(image)
        self.image = self.jugador_frame_izq[0]

        self.rect = self.image.get_rect()



class MovingPlatform(Enemigo):
    """ This is a fancier platform that can actually move. """
    mover_x = 0
    mover_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    nivel = None
    player = None

    def update(self):
        """ Move the platform.
            If the jugador is in the way, it will shove the jugador
            out of the way. This does NOT handle what happens if a
            platform shoves a jugador into another object. Make sure
            moving platforms have clearance to push the jugador around
            or add code to handle what happens if they don't. """

        self.calc_grav()

        #self.mover_x = -2

        # Move left/right
        self.rect.x += self.mover_x

        pos = self.rect.x
        frame = (pos // 30) % len(self.jugador_frame_izq)
        self.image = self.jugador_frame_izq[frame]


        #ACA ES CUANDO CHOCAMOS CON EL ENEMIGO. HACER LAS ACCIONES QUE SE QUIERAN.
        # Primera accion: Eliminar el enemigo
        # Segunda accion: Quitar puntos.
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            self.kill()
            self.player.vida -= 10


        # Verficiamos si colisionamos con alguna plataforma
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.platform_list, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_x > 0:
                self.rect.right = block.rect.left
            elif self.mover_x < 0:
                self.rect.left = block.rect.right
 
        self.rect.y += self.mover_y

        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.platform_list, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_y > 0:
                self.rect.bottom = block.rect.top
            elif self.mover_y < 0:
                self.rect.top = block.rect.bottom

            self.mover_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.mover_x
                
    def calc_grav(self):
        """ Calcula el efecto de la gravedad. """
        if self.mover_y == 0:
            self.mover_y = 2
        else:
            self.mover_y += .34

        # Verificamos si estamos en el suelo.
        if self.rect.y >= constantes.LARGO_PANTALLA - self.rect.height and self.mover_y >= 1:
            self.mover_y = 1
            self.rect.y = constantes.LARGO_PANTALLA - self.rect.height
            
            



