from sys import exit

import pygame
from pygame.locals import QUIT, Rect

SCREEN = 640, 480
FLAGS = 0
COLOR_BITS = 32
H = 80


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN, FLAGS, COLOR_BITS)
    scales = create_scales()
    game = Game(screen, scales)
    while True:
        game.run()
        

def create_scales():
    surfaces = [pygame.surface.Surface((SCREEN[0], H))] * 3
    for x in range(SCREEN[0]):
        c = int((x / 639.) * 255.)
        r = (c, 0, 0)
        g = (0, c, 0)
        b = (0, 0, c)
        line_rect = Rect(x, 0, 1, H)
        for s, rgb in zip(surfaces, [r, g, b]):
            pygame.draw.rect(s, rgb, line_rect)
    return surfaces


class Game:
    def __init__(self, screen, scales):
        self.screen = screen
        self.scales = scales
        self.color = [127] * 3

    def run(self):
        self._handle_events()
        self.screen.fill((0, 0, 0))
        for i, scale in enumerate(self.scales):
            self.screen.blit(scale, (0, i * H))
        self._adjust_color_component()
        self._draw_sliders()
        pygame.draw.rect(
            self.screen, tuple(self.color), (0, 3*H, SCREEN[0], 3*H))
        pygame.display.update()
        
    def _handle_events(self):
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                exit()

    def _adjust_color_component(self):
        x, y = pygame.mouse.get_pos()
        # If mouse pressed on a slider, adj color component
        if pygame.mouse.get_pressed()[0]:
            for component in range(3):
                if (y > component*H and y < (component + 1)*H):
                    self.color[component] = int((x / 639.) * 255.)
                pygame.display.set_caption(f'Color Test: (tuple(self.color))')

    def _draw_sliders(self):
        # Draw a circle for ea slider to repr current setting
        for component in range(3):
            pos = (int((self.color[component] / 255.) * 639),
                   component*H + (H/2))
            pygame.draw.circle(self.screen, (255, 255, 255), pos, 20)

                
if __name__ == '__main__':
    main()
