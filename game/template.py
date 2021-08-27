from sys import exit

import pygame
from pygame.locals import QUIT


SCREEN = (640, 480)
FLAGS = 0
COLOR_BITS = 32


def main():
    pygame.init()
    game = Game()
    game.run()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN, FLAGS, COLOR_BITS)
        
    def run(self):
        while True:
            self._handle_events()

    def _handle_events():
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()


if __name__ == '__main__':
    main()
