import pygame
from map import Map
from constants import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_NAME, "lol")

        self.map = Map()

        self.game_running = True

    def run(self):
        clock = pygame.time.Clock()
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False

            self.screen.fill((0, 0, 0))
            self.map.run()
            pygame.display.update()

            clock.tick(FPS)


if __name__ == "__main__":
    pygame.init()
    Game().run()
