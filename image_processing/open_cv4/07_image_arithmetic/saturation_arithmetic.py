import cv2
import numpy as np


x = np.uint8([250])
y = np.uint8([50])
res_opencv = cv2.add(x, y)
print(res_opencv) # [[255]]
res_np = x + y    # 8 bit int so 300 % 256 = 44
print(res_np)


# Image Addition and Subtraction
M = np.ones(image.shape, dtype='uint8') * 60
added_image = cv2.add(image, M)
scalar = np.ones((1, 3), dtype='float') * 110
added_image = cv2.add(image, scalar)
