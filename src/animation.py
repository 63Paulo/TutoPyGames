import pygame
from pygame.sprite import AbstractGroup

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f"sprite/{name}.png")
        self.images = {
            'down' : self.get_image(0,0),
            'left' : self.get_image(0,32),
            'right' : self.get_image(0,64),
            'up' : self.get_image(0, 96)
        }

    def get_image(self,x,y):
        image = pygame.Surface([32,32])
        image.blit(self.sprite_sheet, (0,0), (x,y,32,32))
        return image