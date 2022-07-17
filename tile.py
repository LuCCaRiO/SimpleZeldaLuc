import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, image, pos):
        super(Tile, self).__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
