import numpy as np
import cv2


def get_random_color():
    return np.random.randint(0, 256, size=3).tolist()

# locations of hours
hours_orig = np.array([
    (620, 320), (580, 470), (470, 580), (320, 620), (170, 580), ( 60, 470),
    ( 20, 320), ( 60, 170), (169,  61), (319,  20), (469,  60), (579, 169)])
hours_dest = np.array([
    (600, 320), (563, 460), (460, 562), (320, 600), (180, 563), ( 78, 460),
    ( 40, 320), ( 77, 180), (179,  78), (319,  40), (459,  77), (562, 179)])

# Draw hour marks
for i in range(12):
    cv2.line(image,
             array_to_tuple(hours_orig[i]),
             array_to_tuple(hours_dest[i]),
             get_random_color(),
             3)
cv2.rectangle(image, (150, 175), (490, 270), get_random_color(), -1)
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

