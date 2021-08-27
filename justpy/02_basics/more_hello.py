import justpy as jp
import numpy as np


def hello():
    wp = jp.WebPage()
    for i in range(1, 11):
        jp.P(text=f'{i}) Hello, World{i * "!"}',
             a=wp,
             style=f'font-size: {5*i}px; color: {rand_color()}')
    return wp


def rand_color(alpha=False):
    digits = list('0123456789abcdef')
    n = 8 if alpha else 6
    return '#' + ''.join(np.random.choice(digits, size=n))


jp.justpy(hello)
