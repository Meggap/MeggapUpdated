import pygame

from funciones_spritesheet import SpriteSheet, SpriteSheetNotas
import constantes

class Negro (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        
        self.image = sprite_sheet.get_image(0,0,20,34)
      
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.puntosdenota = 1
            
class Amarillo (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(20,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 1
            
class Azul (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(40,0,20,34)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 1
            
class Naranja (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(60,0,20,34)
                                            
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 1
        
class Rojo (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(80,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 1
class Verde (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(100,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 1
class Violeta (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(120,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 1
class Negro2 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(140,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 2
class Amarillo2 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(160,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 2
class Azul2 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(180,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 2
class Naranja2 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(200,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 2
class Rojo2 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(220,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 2
class Verde2 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(240,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 2
class Violeta2 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(260,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 2
class Negro3 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(280,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 3
class Amarillo3 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(300,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 3    
class Azul3 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(320,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 3
class Naranja3 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(340,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 3
class Rojo3 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(360,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 3
class Verde3 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(380,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 3
class Violeta3 (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/notasspritesheet.png")
        self.image = sprite_sheet.get_image(400,0,20,34)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 3
class ClaveSol (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/clavedesol.png")
        self.image = sprite_sheet.get_image(0,0,82,40)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        puntosdenota = 10
