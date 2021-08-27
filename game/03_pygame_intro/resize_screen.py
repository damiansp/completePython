from sys import exit

import pygame
from pygame.locals import FULLSCREEN, K_f, KEYDOWN, QUIT, RESIZABLE, VIDEORESIZE


IMG = '../images'
BKG = f'{IMG}/sushiplate.jpg'
WINDOW_SIZE = (640, 480)
FLAGS = RESIZABLE
COLOR_BITS = 32


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE, FLAGS, COLOR_BITS)
    bkg = pygame.image.load(BKG).convert()
    fullscreen = False
    game = Game(screen, bkg, fullscreen)
    while True:
        game.run()


class Game:
    def __init__(self, screen, bkg, fullscreen):
        self.screen = screen
        self.bkg = bkg
        self.bkg_h = self.bkg.get_height()
        self.bkg_w = self.bkg.get_width()
        self.fullscreen = fullscreen
        self.size = WINDOW_SIZE
        self.events = [KEYDOWN, QUIT, VIDEORESIZE]

    def run(self):
        for e in pygame.event.get():
            if e.type in self.events:
                self._handle_event(e)
        self._blit()
        pygame.display.update()

    def _handle_event(self, e):
        try:
            {QUIT: self._quit_game,
             KEYDOWN: self._toggle_fullscreen,
             VIDEORESIZE: self._resize}[e.type](e)
        except KeyError:
            print('No event defined for', e.type)

    def _quit_game(self, e):
        pygame.quit()
        exit()
    
    def _toggle_fullscreen(self, e):
        if e.key == K_f:
            self.fullscreen = not self.fullscreen
            if self.fullscreen:
                self.screen = pygame.display.set_mode(
                    WINDOW_SIZE, FULLSCREEN, COLOR_BITS)
            else:
                self.screen = pygame.display.set_mode(
                    WINDOW_SIZE, FLAGS, COLOR_BITS)

    def _resize(self, e):
        self.size = e.size
        self.screen = pygame.display.set_mode(self.size, RESIZABLE, COLOR_BITS)
        pygame.display.set_caption(f'Resized to {self.size}')

    def _blit(self):
        W, H = self.size
        for y in range(0, H, self.bkg_h):
            for x in range(0, W, self.bkg_w):
                self.screen.blit(self.bkg, (x, y))

                
if __name__ == '__main__':
    main()
