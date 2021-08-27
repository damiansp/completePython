from sys import exit

import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT


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
        self.points = []
        
    def run(self):
        while True:
            self._handle_events()
            self.screen.fill((255, 255, 255))
            if len(self.points) > 2:
                pygame.draw.polygon(self.screen, (255, 0, 0), self.points)
            for point in self.points:
                pygame.draw.circle(self.screen, (0, 0, 255), point, 5)
            pygame.display.update()

    def _handle_events(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                self.points.append(e.pos)


if __name__ == '__main__':
    main()
