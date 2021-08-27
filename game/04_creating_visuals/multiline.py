from sys import exit

import pygame
from pygame.locals import MOUSEMOTION, QUIT


SCREEN = (640, 480)
FLAGS = 0
COLOR_BITS = 32


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN, FLAGS, COLOR_BITS)
    run(screen)

    
def run(screen):
    points = []
    while True:
        points = handle_events(points)
        screen.fill((0, 0, 0))
        if len(points) > 1:
            pygame.draw.lines(screen, (0, 255, 255), False, points, 2)
        pygame.display.update()


def handle_events(points):
    for e in pygame.event.get():
        events = {QUIT: quit_game,
                  MOUSEMOTION: add_pos}
        if e.type in events:
            points = events[e.type](e.pos, points)
    return points


def quit_game(pos, points):
    if e.type == QUIT:
        pygame.quit()
        exit()


def add_pos(pos, points):
    points.append(pos)
    if len(points) > 100:
        del points[0]
    return points


if __name__ == '__main__':
    main()
