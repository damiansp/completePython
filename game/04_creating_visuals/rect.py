from random import randint
from sys import exit

import pygame
from pygame.locals import QUIT, Rect


SCREEN = (640, 480)
FLAGS = 0
COLOR_BITS = 32


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN, FLAGS, COLOR_BITS)
    screen = draw_rand_rects(screen)
    pygame.display.update()
    run()

    
def draw_rand_rects(screen):
    screen.lock()
    for count in range(10):
        rand_color = [randint(0, 255) for _ in range(3)]
        rand_pos = [randint(0, dim - 1) for dim in SCREEN]
        rand_size = [dim - 1 - randint(pos, dim)
                     for (pos, dim) in zip(rand_pos, SCREEN)]
        pygame.draw.rect(screen, rand_color, Rect(rand_pos, rand_size))
    screen.unlock()
    return screen


def run():
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()


if __name__ == '__main__':
    main()
