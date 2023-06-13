import pygame
import pytmx
import pyscroll
from pygame.locals import *


from player import Player

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Pygamon - Aventure')

        tmx_data = pytmx.util_pygame.load_pygame('carte.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=3)
        self.group.add(self.player)

    def handle_input(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            self.player.move_up()
        elif pressed[pygame.K_s]:
            self.player.move_down()
        elif pressed[pygame.K_q]:
            self.player.move_left()
        elif pressed[pygame.K_d]:
            self.player.move_right()


    def run(self):
        running = True

        while running:
            
            self.handle_input()
            self.group.center(self.player.rect)
            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()

            for event  in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()