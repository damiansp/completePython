import pygame
from pygame.locals import *

W, H = 500, 500
FONT = pygame.font.SysFont('Arial', 30)
ORANGE = (255, 100, 10)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
N_ROWS = 6
N_COLS = 6
FRAME_RATE = 60


def main():
    pygame.init()
    window = pygame.display.set_mode((W, H))
    pygame.display.set_caption('Brickabrack')
    clock = pygame.time.Clock()
    my_ball = False
    game_over = 0
    score = 0
    user_paddle = paddle()


class Ball():
    def __init__(self, x, y, r=10):
        self.r = r
        self,x = x - self.r
        self.y = y - 50
        self.rect = Rect(self.x, self.y, 2 * self.r, 2 * self.r)
        self.x_speed = 4
        self.y_speed = -4
        self.max_speed = 5
        self.game_over = 0
        self.collision_thresh = 5
        
    def move(self):
        block_obj = Block.bricks
        brick_destroyed = 1
        count_row = 0
        for row in block_obj:
            count_item = 0
            for item in row:
                # collision with window?
                if self.rect.colliderect(item[0]):
                    if (self._collide_top(item[0])
                        or self._collide_bottom(item[0])):
                        self.y_speed *= -1
                    if (self._collide_left(item[0])
                        or self._collide_right(item[0])):
                        self.x_speed *= 1
                    if block_obj[count_row][count_item][1] > 1:
                        block_obj[count_row][count_item][1] -= 1
                    else:
                        block_obj[count_row][count_item][0] = (0, 0, 0, 0)
                if block_obj[count_row][count_item][0] != (0, 0, 0, 0):
                    brick_destroyed = 0
                count_item += 1
            count_row += 1
        if brick_destroyed == 1:
            self.game_over = 1
        # collision w bricks?
        if self.rect.left < 0 or self.rect.right > W:
            self.x_speed *= 1
        if self.rect.top < 0:
            self.y_speed *= -1
        if self.rect.bottom > H:
            self.game_over = -1
        # collision w paddle
        if self.rect.coliderect(user_paddle):
            if self._collide_top(user_paddle.rect):
                self.y_speed *= -1
                self.x_speed += user_paddle.direction
                if self.x_speed > self.max_speeed:
                    self.x_speed = self.max_speed
                elif self.x_speed < 0 and self.x_speed < -self.max_speed:
                    self.x_speed = -self.max_speed
                else:
                    self.x_speed *= -1
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        return self.game_over
            
    def _collide_top(self, item):
        return (
            abs(self.rect.bottom - item.top) < self.collision_thresh
            and self.y_speed > 0)

    def _collide_bottom(self, item):
        return (
            abs(self.rect.top - item.bottom) < self.collision_thresh
            and self.y_speed < 0)

    def _collide_left(self, item):
        return (
            abs(self.rect.right - item.left) < self.collision_thresh
            and self.y_speed > 0)

    def _collide_right(self, item):
        return (
            abs(self.rect.left - item.right) < self.collision_thresh
            and self.y_speed < 0)

    def draw(self):
        #TODO


if __name__ == '__main__':
    main()
