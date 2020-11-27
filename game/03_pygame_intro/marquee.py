from sys import exit

import pygame
from pygame.locals import QUIT


IMG = '../images'
BKG = f'{IMG}/sushiplate.jpg'
SCREEN_SIZE = 640, 480
FLAGS = 0
COLOR_BITS = 32
MARQUEE = '     This is a marquee demo.  So scrolly!     '
FONT_SIZE_PX = 80
ANTIALIAS = True
TXT_COL = 0, 0, 255


def main():
    pygame.init()
    game = Game()
    game.run()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.font = pygame.font.SysFont('arial', FONT_SIZE_PX)
        self.text_surface = self.font.render(MARQUEE, ANTIALIAS, TXT_COL)
        self.W = self.text_surface.get_width()
        self.H = self.text_surface.get_height()
        self.x = 0
        self.y = (SCREEN_SIZE[1] - self.H) / 2
        self.bkg = pygame.image.load(BKG).convert()

    def run(self):
        while True:
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    exit()
            self.screen.blit(self.bkg, (0, 0))
            self._scroll_marquee()

    def _scroll_marquee(self):
        self.x -= 2
        if self.x < -self.W:
            self.x = 0
        x, y = self.x, self.y
        self.screen.blit(self.text_surface, (x, y))
        self.screen.blit(self.text_surface, (x + self.W, y))
        pygame.display.update()

        
if __name__ == '__main__':
    main()
