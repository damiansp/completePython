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
          'rand': get_random_color}


def show(img, title):
    '''Show an image using matplotlib'''
    img_RGB = img[:, :, ::-1]
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


def main():
    DIM = 400
    image = np.zeros((DIM, DIM, 3), dtype='uint8')
    image[:] = colors['light_grey']

    # clip line
    cv2.line(image, (0, 0), (DIM, DIM), get_random_color(), 3)
    cv2.rectangle(image, (0, 0), (100, 100), get_random_color(), 3)
    ret, p1, p2 = cv2.clipLine((0, 0, 100, 100), (0, 0), (DIM, DIM))
    if ret:
        cv2.line(image, p1, p2, get_random_color(), 3)
    show(image, 'clip line')
    
    
    
    

if __name__ == '__main__':
    main()
