#!/usr/bin/env python3
from sys import exit

import pygame
from   pygame.locals import QUIT


IMG = '../images'
BKG = f'{IMG}/sushiplate.jpg'
MOUSE = f'{IMG}/fugu.png'
WINDOW_DIMS = 640, 480
FLAGS = 0
COLOR_BITS = 32


def main():
    screen, bkg, mouse_cursor = init()
    run(screen, bkg, mouse_cursor)
    

def init():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_DIMS, FLAGS, COLOR_BITS)
    pygame.display.set_caption('Hello, Pygame!')
    bkg = pygame.image.load(BKG).convert()
    mouse_cursor = pygame.image.load(MOUSE).convert_alpha()
    return screen, bkg, mouse_cursor


def run(screen, bkg, mouse_cursor):
    CURSOR_DIMS = mouse_cursor.get_width(), mouse_cursor.get_height()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
        screen.blit(bkg, (0, 0))
        x, y = pygame.mouse.get_pos()
        x -= CURSOR_DIMS[0] // 2
        y -= CURSOR_DIMS[1] // 2
        screen.blit(mouse_cursor, (x, y))
        pygame.display.update()


if __name__ == '__main__':
    main()
