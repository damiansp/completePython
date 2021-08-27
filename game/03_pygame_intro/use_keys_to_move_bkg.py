from sys import exit

import pygame
from pygame.locals import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, KEYUP, QUIT


IMG = '../images'
BKG = f'{IMG}/sushiplate.jpg'
WINDOW_DIMS = (640, 480)
FLAGS = 0
COLOR_BITS = 32


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_DIMS, FLAGS, COLOR_BITS)
    bkg = pygame.image.load(BKG).convert()
    x, y = 0, 0
    dx, dy = 0, 0
    while True:
        x, y, dx, dy = run_game(screen, bkg, x, y, dx, dy)

        
def run_game(screen, bkg, x, y, dx, dy):
    for e in pygame.event.get():
        if e.type in [KEYDOWN, KEYUP, QUIT]:
            dx, dy = {KEYDOWN: keydown,
                      KEYUP: keyup,
                      QUIT: quit_game}[e.type](e, dx, dy)
            x += dx
            y += dy
            screen.fill((0, 0, 0))
            screen.blit(bkg, (x, y))
            pygame.display.update()
    return x, y, dx, dy


def keydown(e, dx, dy):
    key = e.key
    dx, dy = {K_LEFT:  (-1,  0),
              K_RIGHT: ( 1,  0),
              K_UP:    ( 0, -1),
              K_DOWN:  ( 0,  1)}[key]
    return dx, dy


def keyup(e, dx, dy):
    return (dx, dy)

def quit_game(e):
    pygame.quit()
    exit()
        
    

if __name__ == '__main__':
    main()
