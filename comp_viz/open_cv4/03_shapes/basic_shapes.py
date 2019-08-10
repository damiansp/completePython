import matplotlib.pyplot as plt
import numpy as np

import cv2

import constant


def get_random_color():
    return np.random.randint(0, 256, size=3).tolist()


colors = {'blue':       constant.BLUE,
          'green':      constant.GREEN,
          'red':        constant.RED,
          'yellow':     constant.YELLOW,
          'magenta':    constant.MAGENTA,
          'cyan':       constant.CYAN,
          'white':      constant.WHITE,
          'grey':       constant.GREY,
          'dark_grey':  constant.DARK_GREY,
          'light_grey': constant.LIGHT_GREY,
          'rand': get_random_color()}


def show(img, title):
    '''Show an image using matplotlib'''
    img_RGB = img[:, :, ::-1]
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


def main():
    image = np.zeros((400, 400, 3), dtype='uint8')
    image[:] = colors['light_grey']
    show(image, 'just grey')
    

if __name__ == '__main__':
    main()
