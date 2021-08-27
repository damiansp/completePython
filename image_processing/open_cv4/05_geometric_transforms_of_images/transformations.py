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


# Affine (e.g., Linear) Transformations
pts_1 = np.float32([[135, 45], [385, 45], [135, 230]])
pts_2 = np.float32([[135, 45], [385, 45], [150, 230]])
M = cv2.getAffineTransform(pts_1, pts_2)
dst_image = cv2.warpAffine(image_points, M, (width, height))


# Perspective Transformation
pts_1 = np.float32([[450, 65], [517, 65], [431, 164], [552, 164]])
pts_2 = np.float32([[  0,  0], [300,  0], [  0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts_1, pts_2)
dst_image = cv2.warpPerspective(image, M, (300, 300))


# Cropping
dst_image = image[80:200, 230:330]
