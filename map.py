import pygame
from player import Player
from tile import Tile
from constants import *


class Map:
    def __init__(self):
        self.visible_sprites = Camera()
        self.obstacle_sprites = pygame.sprite.Group()

        self.player = None
        self.create_map()

    def create_map(self):
        for layer_index in range(len(MAP)):
            for column_index in range(len(MAP[layer_index])):
                for row_index, row in enumerate(MAP[layer_index][column_index]):
                    x = row_index * TILE_SIZE
                    y = column_index * TILE_SIZE
                    if row == "p":

                        self.player = Player([self.visible_sprites], self.obstacle_sprites,
                                             [pygame.image.load("./img/link_sheet/player1.png"),
                                              pygame.image.load("./img/link_sheet/player2.png"),
                                              pygame.image.load("./img/link_sheet/player3.png"),
                                              pygame.image.load("./img/link_sheet/player4.png")], (x, y), 2)
                    if row == "x":
                        Tile([self.visible_sprites, self.obstacle_sprites], pygame.image.load("./img/Wall.png"), (x, y))
                    if row == "g":
                        Tile([self.visible_sprites], pygame.image.load("./img/Grass.png"), (x, y))
                    if row == "h":
                        Tile([self.visible_sprites], pygame.image.load("./img/Grass2.png"), (x, y))

    def run(self):
        self.visible_sprites.update()
        self.visible_sprites.custom_draw(self.player)


class Camera(pygame.sprite.Group):
    def __init__(self):
        super(Camera, self).__init__()
        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(0, TILE_SIZE * len(MAP[0]) - SCREEN_HEIGHT)

    def custom_draw(self, player):
        if SCREEN_WIDTH / 2 >= player.rect.centerx >= SCREEN_WIDTH / 2:
            self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        if SCREEN_HEIGHT / 2 + TILE_SIZE * 5 >= player.rect.centery >= SCREEN_HEIGHT / 2:
            self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for sprite in self.sprites():
            self.screen.blit(sprite.image, sprite.rect.topleft - self.offset)
