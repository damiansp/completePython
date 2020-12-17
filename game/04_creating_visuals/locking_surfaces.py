from random import randint
from sys import exit

import pygame
from pygame.locals import QUIT


SCREEN = 640, 480
FLAGS = 0
COLOR_BITS = 32


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN, FLAGS, COLOR_BITS)
    while True:
        screen = run(screen)

        
def run(screen):
    handle_events()
    rcol = [randint(0, 255) for _ in range(3)]
    print(rcol)

    screen.lock()
    for _ in range(100):
        rpos = (randint(0, SCREEN[0] - 1), randint(0, SCREEN[1] - 1))
        screen.set_at(rpos, rcol)
    screen.unlock()

    pygame.display.update()
    return screen


def handle_events():
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()


if __name__ == '__main__':
    main()
