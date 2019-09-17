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
fonts = [cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_PLAIN,
         cv2.FONT_HERSHEY_DUPLEX, cv2.FONT_HERSHEY_COMPLEX,
         cv2.FONT_HERSHEY_TRIPLEX, cv2.FONT_HERSHEY_COMPLEX_SMALL,
         cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, cv2.FONT_HERSHEY_SCRIPT_COMPLEX]
font_names = ['FONT_HERSHEY_SIMPLEX', 'FONT_HERSHEY_PLAIN',
              'FONT_HERSHEY_DUPLEX', 'FONT_HERSHEY_COMPLEX',
              'FONT_HERSHEY_TRIPLEX', 'FONT_HERSHEY_COMPLEX_SMALL',
              'FONT_HERSHEY_SCRIPT_SIMPLEX', 'FONT_HERSHEY_SCRIPT_COMPLEX']
         

def show(img, title):
    '''Show an image using matplotlib'''
    img_RGB = img[:, :, ::-1]
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


def main():
    DIM = 1200
    image = np.zeros((DIM, DIM, 3), dtype='uint8')
    image[:] = colors['light_grey']
    show(image, 'just grey')

    # lines
    cv2.line(image, (0, 0), (DIM, DIM), colors['green'], 1) # 1=thickness
    cv2.line(image, (0, DIM), (DIM, 0), colors['blue'], 2)
    cv2.line(image, (DIM // 2, 0), (DIM // 2, DIM), colors['red'], 4)
    cv2.line(image, (0, DIM // 2), (DIM, DIM // 2), colors['yellow'], 8)
    show(image, 'lines')

    # rects
    cv2.rectangle(image, (10,   50), ( 60, 300), colors['green'], 3) # 3=thick
    cv2.rectangle(image, (80,   50), (130, 300), colors['blue'], -1) # fill
    cv2.rectangle(image, (150,  50), (350, 100), colors['red'],  -1)
    cv2.rectangle(image, (150, 150), (350, 300), colors['cyan'], 10)
    show(image, 'rectangles')

    # circles
    image.fill(255) # all white
    cv2.circle(
        image, center=(50, 50), radius=20, color=colors['green'], thickness=3)
    cv2.circle(image, (100, 100), 50, colors['blue'], -1)
    cv2.circle(image, (200, 200), 60, colors['magenta'], 10)
    cv2.circle(image, (300, 300), 70, colors['cyan'], -1)
    show(image, 'circles')

    # text
    cv2.putText(image,
                'Mastering OpenCV4 with Python',
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,        # fontScale
                get_random_color(),
                2,          # thickness
                cv2.LINE_4) # lineType
                            # bottomLeftOrigin=False (omitted)
    cv2.putText(image,
                'Mastering OpenCV4 with Python',
                (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,       # fontScale
                get_random_color(),
                2,
                cv2.LINE_8)
    cv2.putText(image,
                'Mastering OpenCV4 with Python',
                (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,       # fontScale
                get_random_color(),
                2,
                cv2.LINE_AA)
    show(image, 'text')

    # fonts
    image.fill(255)
    pos = [10, 30]
    for i in range(8):
        col = get_random_color()
        cv2.putText(image,
                    font_names[i],
                    tuple(pos),
                    fonts[i],
                    1.1,
                    col,
                    2,
                    cv2.LINE_AA)
        pos[1] += 40
        cv2.putText(image,
                    font_names[i].lower(),
                    tuple(pos),
                    fonts[i],
                    1.1,
                    col,
                    2,
                    cv2.LINE_AA)
        pos[1] += 40
    show(image, 'fonts')

    # More text-related functions
    image.fill(255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2.5
    thickness = 5
    text = 'abcdefghijklmnopqrstuvwxyz'
    radius = 10

    # Get size of text
    ret, baseline = cv2.getTextSize(text, font, font_scale, thickness)
    # Width and height
    text_width, text_height = ret
    # Center text in image
    text_x = int(round((image.shape[1] - text_width) / 2)) 
    text_y = int(round((image.shape[0] - text_height) / 2)) # y is 0?
    # Draw center point for ref
    cv2.circle(image, (text_x, text_y), radius, get_random_color(), -1)
    # Bounding box for text
    cv2.rectangle(image,
                  (text_x, text_y + baseline),
                  (text_x + text_width - thickness, text_y - text_height),
                  get_random_color(),
                  thickness)
    # Draw baseline
    cv2.line(
        image,
        (text_x, text_y + int(round(thickness / 2))),
        (text_x + text_width - thickness, text_y + int(round(thickness / 2))),
        get_random_color(),
        thickness)
    # Write the text
    cv2.putText(image,
                text,
                (text_x, text_y),
                font, font_scale,
                get_random_color(),
                thickness)
    show(image, 'Text params')
    
    

if __name__ == '__main__':
    main()
