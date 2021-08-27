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

    # arrows
    cv2.arrowedLine(image,
                    (50, 50),
                    (200, 50),
                    colors['red'],
                    thickness=3,
                    line_type=8, # 8, 4, none: connected CV_AA: anitaliased
                    shift=0,
                    tipLength=0.1)
    cv2.arrowedLine(
        image, (50, 120), (200, 120), colors['green'], 3, cv2.LINE_AA, 0, 0.3)
    cv2.arrowedLine(image, (50, 200), (200, 200), colors['blue'], 4, 6, 0, 0.3)
    show(image, 'arrows')

    # ellipses
    # img, center, axes, angle, startAngle, endAngle, color, thickness,
    # lineType, shift
    cv2.ellipse(image, ( 80,  80), (60, 40),  0, 0, 360, colors['red'],      -1)
    cv2.ellipse(image, ( 80, 200), (80, 40),  0, 0, 360, colors['green'],     3)
    cv2.ellipse(image, ( 80, 200), (10, 40),  0, 0, 360, colors['blue'],      3)
    cv2.ellipse(image, (200, 200), (10, 40),  0, 0, 180, colors['yellow'],    3)
    cv2.ellipse(image, (200, 100), (10, 40),  0,10, 360, colors['cyan'],      2)
    cv2.ellipse(image, (250, 250), (30, 30),  0, 0, 360, colors['magenta'],   3)
    cv2.ellipse(image, (250, 100), (20, 40), 45, 0, 350, colors['dark_grey'], 3)
    show(image, 'ellipses')

    # polygons
    # img, pts, isClosed, color, thickness, lineType, shift
    pts = np.array([[250, 5], [220, 80], [280, 80]], np.int32)
    pts = pts.reshape((-1, 1, 2)) # n_vertex (3), 1, 2
    print(pts.shape)
    cv2.polylines(image, [pts], True, get_random_color(), 3)
    show(image, 'polygon')

    # shift param
    DIM = 600
    image = np.zeros((DIM, DIM, 3), dtype='uint8')
    image[:] = colors['light_grey']
    shift = 2
    factor = 2 ** shift
    print(f'factor: {factor}')
    # circle with r = 300
    cv2.circle(image,
               (int(round(299.99 * factor)), int(round(299.99 * factor))),
               300 * factor,
               colors['red'],
               1,
               shift=shift)
    cv2.circle(image, (299, 299), 300, colors['green'], 1)
    show(image, 'circle/shift')

    DIM = 600
    image = np.zeros((DIM, DIM, 3), dtype='uint8')
    image[:] = colors['light_grey']
    draw_float_circle(image,
                      (299, 299),
                      300,
                      shift=0,
                      color=colors['red'])
    draw_float_circle(image,
                      (299.9, 299.9),
                      300,
                      shift=1,
                      color=colors['green'])
    draw_float_circle(image,
                      (299.99, 299.99),
                      300,
                      shift=2,
                      color=colors['blue'])
    draw_float_circle(image,
                      (299.999, 299.999),
                      300,
                      shift=3,
                      color=colors['yellow'])
    show(image, 'Float Circles')
                      
    

def draw_float_circle(img, center, radius, color,  shift):
    '''wrapper to draw float-coord circle'''
    factor = 2 ** shift
    center = (int(round(center[0] * factor)), int(round(center[1] * factor)))
    radius = int(round(radius * factor))
    cv2.circle(img, center, radius, color, thickness=1, lineType=8, shift=shift)

    
if __name__ == '__main__':
    main()
