from   datetime import datetime
import math

import matplotlib.pyplot as plt
import numpy as np
import cv2

import constant


def get_random_color():
    return np.random.randint(0, 256, size=3).tolist()


def show(img, title):
    '''Show an image using matplotlib'''
    img_RGB = img[:, :, ::-1]
    plt.imshow(img_RGB)
    plt.title(title)
    plt.show()


DIM = 640
image = np.zeros((DIM, DIM, 3), dtype='uint8')
image[:] = constant.WHITE


# locations of hours
hours_orig = np.array([
    (620, 320), (580, 470), (470, 580), (320, 620), (170, 580), ( 60, 470),
    ( 20, 320), ( 60, 170), (169,  61), (319,  20), (469,  60), (579, 169)])
hours_dest = np.array([
    (600, 320), (563, 460), (460, 562), (320, 600), (180, 563), ( 78, 460),
    ( 40, 320), ( 77, 180), (179,  78), (319,  40), (459,  77), (562, 179)])

# Draw hour marks
TICK_COLOR = get_random_color()
for i in range(12):
    cv2.line(image,
             tuple(hours_orig[i]),
             tuple(hours_dest[i]),
             TICK_COLOR,
             3)
cv2.rectangle(image, (140, 175), (500, 270), get_random_color(), -1)
TEXT_COLOR = get_random_color()
cv2.putText(image,
            'A Super Fancy Clock',
            (150, 200),
            1,
            2,
            TEXT_COLOR,
            1,
            cv2.LINE_AA)
cv2.putText(
    image, 'Using OpenCV 4', (210, 250), 1, 2, TEXT_COLOR, 1, cv2.LINE_AA)
image_original = image.copy()

# Get current data
NOW = datetime.now()
NOW_TIME = NOW.time()
hour = math.fmod(NOW_TIME.hour, 12)
minute = NOW_TIME.minute
second = NOW_TIME.second

# Transform time to angles
second_angle = math.fmod(second * 6 + 270, 360)
minute_angle = math.fmod(minute * 6 + 270, 360)
hour_angle = math.fmod(30*hour + minute/2 + 270, 360)

# Draw hands
second_x = round(320 + 310 * math.cos(second_angle * 3.14 / 180))
second_y = round(320 + 310 * math.sin(second_angle * 3.14 / 180))
cv2.line(image, (320, 320), (second_x, second_y), get_random_color(), 2)

minute_x = round(320 + 260 * math.cos(minute_angle * 3.14 / 180))
minute_y = round(320 + 260 * math.sin(minute_angle * 3.14 / 180))
cv2.line(image, (320, 320), (minute_x, minute_y), get_random_color(), 8)

hour_x = round(320 + 220 * math.cos(hour_angle * 3.14 / 180))
hour_y = round(320 + 220 * math.sin(hour_angle * 3.14 / 180))
cv2.line(image, (320, 320), (hour_x, hour_y), get_random_color(), 10)

CIRCLE_COLOR = get_random_color()
cv2.circle(image, (320, 320), 10, CIRCLE_COLOR, -1)
cv2.circle(image, (320, 320), 315, CIRCLE_COLOR, 4)
show(image, 'Clock')
