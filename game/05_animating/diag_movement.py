from sys import exit

import pygame
from pygame.locals import QUIT

W, H = 640, 480
SCREEN = (W, H)
FLAGS = 0
COLOR_BITS = 32
MAX_FRAME_RATE = 30
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
        self.clock = pygame.time.Clock()
        self.bkg = pygame.image.load(BKG).convert()
        self.sprite = pygame.image.load(SPRITE)
        self.x, self.y = 100, 100 # sprite coords
        self.speed_x, self.speed_y = 133, 170 # px/s
                
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
        self.screen.blit(self.sprite, (self.x, self.y))
        time_passed = self.clock.tick(MAX_FRAME_RATE)
        time_passed_s = time_passed / 1000.
        self.x += self.speed_x * time_passed_s
        self.y += self.speed_y * time_passed_s
        # Reset coords when off-screen
        if self.x > W - self.sprite.get_width():
            self.speed_x *= -1
            self.x = W - self.sprite.get_width()
        elif self.x < 0:
            self.speed_x *= -1
            self.x = 0
        if self.y > H - self.sprite.get_height():
            self.speed_y *= -1
            self.y = H - self.sprite.get_height()
        elif self.y < 0:
            self.speed_y *= -1
            self.y = 0
            
            
if __name__ == '__main__':
    main()
