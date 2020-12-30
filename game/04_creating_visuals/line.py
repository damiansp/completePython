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
        screen.fill((0, 0, 0))
        mouse_pos = pygame.mouse.get_pos()
        screen = draw_lines(screen, mouse_pos, step=20)
        pygame.display.update()


def handle_events():
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            exit()


def draw_lines(screen, pos, step=20):
    for x in range(0, SCREEN[0], step):
        pygame.draw.line(screen, (255, 0, 255), (x, 0), pos)
        pygame.draw.line(screen, (255, 0, 255), (x, SCREEN[1] - 1), pos)
    for y in range(0, SCREEN[1], step):
        pygame.draw.line(screen, (255, 0, 255), (0, y), pos)
        pygame.draw.line(screen, (255, 0, 255), (SCREEN[0] - 1, y), pos)
    return screen

    

if __name__ == '__main__':
    main()
