import cv2
import numpy as np


kernel_averaging_5x5 = np.ones((5, 5), np.float32) / 25
smooth_image_f2D = cv2.filter2D(image, -1, kernel_averageing_5x5)

# averaging filter
smooth_image_b = cv2.blur(image, (10, 10))
smooth_image_bfi = cv2.boxFilter(image, -1, (10, 10), normalize=True)

# Gaussian filtering
smooth_image_gb = cv2.GaussianBlur(image, (9, 9), 0)

# Median filtering
smooth_image_mb = cv2.medianBlur(image, 9)
