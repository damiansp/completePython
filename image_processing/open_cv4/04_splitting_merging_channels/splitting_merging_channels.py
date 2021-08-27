import cv2


(b, g, r) = cv2.split(image) # expensive op
image_copy = cv2.merge((b, g, r))

b = image[:, :, 0]
image_without_blue = image.copy()
image_without_blue[:, :, 0] = 0

