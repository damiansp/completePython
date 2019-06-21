import cv2
import matplotlib.pyplot as plt


IMG_DIR = 'images'


img_openCV = cv2.imread(f'{IMG_DIR}/logo.png')
b, g, r = cv2.split(img_openCV) # expensive
img_matplotlib = cv2.merge([r, g, b])
plt.subplot(121)
plt.imshow(img_openCV)
plt.title('Channels Reversed')
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.title('Channels Corrected')
plt.show()

B = img_OpenCV[:, :, 0]
G = img_OpenCV[:, :, 1]
R = img_OpenCV[:, :, 2]
img_matplotlib = img_OpenCV[:, , ::-1]
