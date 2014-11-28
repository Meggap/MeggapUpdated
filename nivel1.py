
import pygame
import constantes
import platforms
from levels import Level
from comida import *
import csv
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)
        #Imagen de fondo
        self.background = pygame.image.load("imagenes/fondorasta.jpg").convert()
        
        #Establecemos el sonido de fondo
        #sonido=pygame.mixer.Sound("")
        #sonido.play()
        self.background.set_colorkey(constantes.BLANCO)
        self.level_limit = -15100
        
        #COMIDAS
        
        self.lista_de_comidas.add(Negro(300,535))
        self.lista_de_comidas.add(Amarillo2(500,280))
        self.lista_de_comidas.add(Azul3(1820,250))
        self.lista_de_comidas.add(Rojo2(1580,430))
        self.lista_de_comidas.add(Naranja(1110,140))
        self.lista_de_comidas.add(Verde(1820,430))
        self.lista_de_comidas.add(Violeta3(1420,535))
        self.lista_de_comidas.add(Rojo(2050,520))
        self.lista_de_comidas.add(Azul(2150,520))
        self.lista_de_comidas.add(Verde3(2250,520))
        #self.lista_de_comidas.add(Celeste(2620,520))
        self.lista_de_comidas.add(Naranja2(2800,520))
        self.lista_de_comidas.add(Violeta(2620,380))
        self.lista_de_comidas.add(Amarillo(2800,380))
        self.lista_de_comidas.add(Rojo2(3100,420))
        self.lista_de_comidas.add(Azul2(3120,250))
        self.lista_de_comidas.add(Rojo(3550,70))
        self.lista_de_comidas.add(Verde2(3500,70))
        self.lista_de_comidas.add(Naranja3(3400,500))
        #self.lista_de_comidas.add(Celeste(3600,500))
        self.lista_de_comidas.add(Amarillo(3800,500))
        self.lista_de_comidas.add(Rojo2(4155,120))
        self.lista_de_comidas.add(Azul2(4800,500))
        self.lista_de_comidas.add(Verde3(4600,200))
        self.lista_de_comidas.add(Violeta(4900,50))
        self.lista_de_comidas.add(Amarillo(4950,50))
        self.lista_de_comidas.add(Rojo2(5150,500))
        self.lista_de_comidas.add(Naranja3(5000,500))
        self.lista_de_comidas.add(Rojo(5245,270))
        self.lista_de_comidas.add(Violeta3(5600,380))
        self.lista_de_comidas.add(Verde2(5500,520))
        self.lista_de_comidas.add(Azul(5700,520))
        self.lista_de_comidas.add(Azul2(6300,430))
        self.lista_de_comidas.add(Amarillo(6500,430))
        self.lista_de_comidas.add(Naranja3(6600,430))
        self.lista_de_comidas.add(Verde(6400,150))
        self.lista_de_comidas.add(Rojo3(7100,420))
        self.lista_de_comidas.add(Azul(7380,400))
        self.lista_de_comidas.add(Violeta3(7500,250))
        self.lista_de_comidas.add(Amarillo2(7750,200))
        self.lista_de_comidas.add(Azul2(7799,520))
        self.lista_de_comidas.add(Rojo2(8180,230))
        self.lista_de_comidas.add(Verde2(8400,100))
        self.lista_de_comidas.add(Naranja(8600,300))
        self.lista_de_comidas.add(Rojo3(8800,300))
        self.lista_de_comidas.add(Azul3(9100,480))
        self.lista_de_comidas.add(Violeta2(9200,490))
        self.lista_de_comidas.add(Verde3(9400,400))
        self.lista_de_comidas.add(Naranja2(9500,300))
        self.lista_de_comidas.add(Azul2(9600,400))
        

        #Artefactos
        autorojo = pygame.image.load("imagenes/auto3.png").convert()
        autorojo.set_colorkey(constantes.BLANCO)
        #autorojo = pygame.transform.rotate(autorojo,90)
        self.background.blit(autorojo, (1980, 500))

        # ubicacion de las plataformas.
        level = [  ]
        with open ("parametros/nivel1.csv", "rb") as archivo:
            plataformas = csv.DictReader(archivo, delimiter=",")
            for fila in plataformas:
                level.append([eval(fila["tipo"]),int(fila["plataforma_x"]),int(fila["plataforma_y"])])
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        level = [ [platforms.PISO, 100, 0], 
                 [platforms.LADRILLO3, 1550, 444],
                 [platforms.LADRILLO3, 1550, 367],
                 [platforms.LADRILLO3, 1880, 367],
                 [platforms.LADRILLO3, 4300, 444],
                 [platforms.LADRILLO3, 4300, 380],
                 [platforms.LADRILLO3, 4300, 300],
                 [platforms.LADRILLO3, 6900, 444],
                 [platforms.LADRILLO3, 6900, 380],
                 [platforms.LADRILLO3, 8890, 444],
                 [platforms.LADRILLO3, 8890, 380],
                 [platforms.LADRILLO3, 11390, 270],
                 #[platforms.LADRILLO3, 11000, 435]

                  ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.VerticalPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

            #Add a custom moving platform
        block = platforms.MovingPlatform(platforms.LADRILLO3)
        block.rect.x = 690
        block.rect.y = 375
        block.boundary_left = 690
        block.boundary_right = 800
        block.mover_x = 1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.LADRILLO2)
        block.rect.x = 3300
        block.rect.y = 200
        block.boundary_left = 3300
        block.boundary_right = 3580
        block.mover_x = 1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms.MovingPlatform(platforms.LADRILLO1)
        block.rect.x = 4150
        block.rect.y = 180
        block.boundary_top = 180
        block.boundary_bottom = 490
        block.mover_y = 1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.LADRILLO3)
        block.rect.x = 4850
        block.rect.y = 100
        block.boundary_left = 4850
        block.boundary_right = 4950
        block.mover_x = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms.MovingPlatform(platforms.LADRILLO1)
        block.rect.x = 4650
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 490
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms.MovingPlatform(platforms.LADRILLO1)
        block.rect.x = 6700
        block.rect.y = 180
        block.boundary_top = 180
        block.boundary_bottom = 455
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.LADRILLO2)
        block.rect.x = 8350
        block.rect.y = 120
        block.boundary_top = 120
        block.boundary_bottom = 400
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms.MovingPlatform(platforms.LADRILLO3)
        block.rect.x = 10400
        block.rect.y = 300
        block.boundary_left = 10400
        block.boundary_right = 10700
        block.mover_x = 1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.LADRILLO1)
        block.rect.x = 12500
        block.rect.y = 320
        block.boundary_top = 320
        block.boundary_bottom = 410
        block.mover_y = 1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.LADRILLO1)
        block.rect.x = 12500
        block.rect.y = 320
        block.boundary_ = 320
        block.boundary_bottom = 410
        block.mover_y = 1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
