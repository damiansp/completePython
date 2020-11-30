from   sys import exit

import pygame
from   pygame.locals import QUIT

from   color_utils import lerp


SCREEN_SIZE = (640, 480)
FLAGS = 0
COLOR_BITS = 32


def main():
    pygame.init()
    color1 = (221,  99, 20)
    color2 = ( 96, 130, 51)
    factor = 0.
    game = Game(color1, color2, factor)
    game.run()
    

    
class Game:
    def __init__(self, color1, color2, factor):
        self.screen = pygame.display.set_mode(SCREEN_SIZE, FLAGS, COLOR_BITS)
        self.color1 = color1
        self.color2 = color2
        self.factor = factor

    def run(self):
        while True:
            self._handle_events()
            self.screen.fill((255, 255, 255))
            tri = [(0, 120), (639, 100), (639, 140)]
            pygame.draw.polygon(self.screen, (0, 255, 0), tri)
            pygame.draw.circle(
                self.screen, (0, 0, 0), (int(self.factor * 639.), 120), 10)
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                self.factor = x / 639.
                pygame.display.set_caption(
                    f'PyGame Color Blend: {self.factor:.3f}')
            color = self._blend_colors()
            pygame.draw.rect(self.screen, color, (0, 240, 640, 240))
            pygame.display.update()

    def _handle_events(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()

    def _blend_colors(self):
        color = [lerp(c1, c2, self.factor)
                 for c1, c2 in zip(self.color1, self.color2)]
        return color

if __name__ == '__main__':
    main()
