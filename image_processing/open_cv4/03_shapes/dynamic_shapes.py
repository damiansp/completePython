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


def main():
    DIM = 800
    image = np.zeros((DIM, DIM, 3), dtype='uint8')
    image[:] = colors['white']
    cv2.namedWindow('Image mouse')
    cv2.setMouseCallback('Image mouse', draw_circle)

    
def show(img, title):
    '''Show an image using matplotlib'''
    img_RGB = img[:, :, ::-1]
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


def draw_circle(event, x, y, flags, param):
    # mouse-callback
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('Event: Double-click')
        cv2.circle(image, (x, y), 10, get_random_color(), -1)
    if event == cv2.EVENT_MOUSEMOVE:
        print('Event: Mouse move')
    if event == cv2.EVENT_LBUTTONUP:
        print('Event: Button-up')
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Event: Button-down')


if __name__ == '__main__':
    main()
