"""
Module for managing platforms.
"""
import pygame

from funciones_spritesheet import SpriteSheetPlataformas, SpriteSheetNotas

# These constantes define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

LADRILLO1            = (0, 0, 65, 40)
LADRILLO2           = (65, 0, 90, 33)
LADRILLO3          = (0, 39, 130, 24)
PISO               = (0,104,6000,33)


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

        self.mover_x = -2

       # Move left/right
        self.rect.x += self.mover_x

        pos = self.rect.x + self.nivel.world_shift
        frame = (pos // 30) % len(self.jugador_frame_izq)
        self.image = self.jugador_frame_izq[frame]

        # See if we hit the jugador
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the jugador. Shove the jugador around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.mover_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.mover_y

        # Check and see if we the jugador
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the jugador. Shove the jugador around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.mover_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom




