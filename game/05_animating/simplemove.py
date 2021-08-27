from sys import exit

import pygame
from pygame.locals import QUIT


SCREEN = (640, 480)
FLAGS = 0
COLOR_BITS = 32
IMG = '../images'
BKG = f'{IMG}/sushiplate.jpg'
SPRITE = f'{IMG}/fugu.png'


def main():
    pygame.init()
    game = Game()
    game.run()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN, FLAGS, COLOR_BITS)
        self.bkg = pygame.image.load(BKG).convert()
        self.sprite = pygame.image.load(SPRITE)
        self.x = 0 # x-coord of sprite
                
    def run(self):
        while True:
            self._handle_events()
            self._animate_sprite()
            pygame.display.update()
                
    def _handle_events(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()

    def _animate_sprite(self):
        # speed of animation will depend on speed of processor
        self.screen.blit(self.bkg, (0, 0))
        self.screen.blit(self.sprite, (self.x, 100))
        self.x += 1
        if self.x > SCREEN[0]: # off screen
            self.x -= (SCREEN[0] + 100) # reset

            
if __name__ == '__main__':
    main()
