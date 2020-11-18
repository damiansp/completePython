from sys import exit

import pygame
from pygame.locals import QUIT

SCREEN_SIZE = (800, 600)
FLAGS = 0
COLOR_BITS = 32


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, FLAGS, COLOR_BITS)
    while True:
        run_game()

        
def run_game():
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()


if __name__ == '__main__':
    main()
