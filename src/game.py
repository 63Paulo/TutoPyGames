import pygame
import pytmx
import pyscroll
from pygame.locals import *


from src.player import Player

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

        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)
    
        enter_house = tmx_data.get_object_by_name('enter_house')
        self.enter_house.rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

    def handle_input(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_s]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_q]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_d]:
            self.player.move_right()
            self.player.change_animation('right')

    def switch_house(self):

        tmx_data = pytmx.util_pygame.load_pygame('housee.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2


        self.walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)
    
        enter_house = tmx_data.get_object_by_name('exit_house')
        self.enter_houserect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)


    def update(self):
        self.group.update()

        if self.player.feet.colliderect(self.enter_house_rect) :
            self.switch_house()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()


    def run(self):

        clock = pygame.time.Clock()

        running = True

        while running:
            
            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event  in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)

        pygame.quit()