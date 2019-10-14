import cv2
import numpy as np


# Scaling
resized_image = cv2.resize(
    image, (width * 2, height * 2), interpolation=cv2.INTER_LINEAR)
dst_image = cv2.resize(
    image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)


# Translating
x = 10
y = -5
M = np.float32([[1, 0, x], [0, 1, y]]) # translation matrix
dst_image = cv2.warpAffine(image, M, (width, height)) # w, h are for output img

height, width = image.shape[:2]
M = np.float32([[1, 0, -200], [0, 1, -30]])
dst_image = cv2.warpAffine(image, M, (width, height))


# Rotation
# (center), deg, scale
M = cv2.getRotationMatrix2D((width / 2., height / 2.), 180, 1) 
dst_image = cv2.warpAffine(image, M, (width, height))
