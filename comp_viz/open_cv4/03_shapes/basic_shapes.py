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
    DIM = 400
    image = np.zeros((DIM, DIM, 3), dtype='uint8')
    image[:] = colors['light_grey']
    show(image, 'just grey')

    cv2.line(image, (0, 0), (DIM, DIM), colors['green'], 1) # 1=thickness
    cv2.line(image, (0, DIM), (DIM, 0), colors['blue'], 2)
    cv2.line(image, (DIM // 2, 0), (DIM // 2, DIM), colors['red'], 4)
    cv2.line(image, (0, DIM // 2), (DIM, DIM // 2), colors['yellow'], 8)
    show(image, 'lines')

    cv2.rectangle(image, (10,   50), ( 60, 300), colors['green'], 3) # 3=thick
    cv2.rectangle(image, (80,   50), (130, 300), colors['blue'], -1) # fill
    cv2.rectangle(image, (150,  50), (350, 100), colors['red'],  -1)
    cv2.rectangle(image, (150, 150), (350, 300), colors['cyan'], 10)
    show(image, 'rectangles')
    
    
    
    

if __name__ == '__main__':
    main()
