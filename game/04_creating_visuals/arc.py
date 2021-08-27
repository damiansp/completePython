from math import pi
from sys import exit

import pygame
from pygame.locals import QUIT


SCREEN = (640, 480)
FLAGS = 0
COLOR_BITS = 32


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN, FLAGS, COLOR_BITS)
    run(screen)

    
def run(screen):
    while True:
        handle_events()
        x, y  = pygame.mouse.get_pos()
        angle = pi * 2 * x/639.
        screen.fill((0, 0, 0))
        pygame.draw.arc(
            screen, (255, 0, 255), (0, 0, SCREEN[0] - 1, SCREEN[1] -1), 0, angle
        )
        pygame.display.update()


def handle_events():
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()


if __name__ == '__main__':
    main()
