import cv2


IMG_DIR = 'images'


img = cv2.imread(f'{IMG_DIR}/logo.png')
dims = img.shape       # 600, 487, 3
n_elements = img.size  # 876600
img_dtype = img.dtype  # uint8
print(f'dims: {dims}\nelements: {n_elements}\ndtype: {img_dtype}')


def show(title, img):
    cv2.imshow(title, img)
    # Keyboard binding function--waits for any keyboard event; wait for arg ms
    # if 0, waits indefinitely    cv2.waitKey(0)
    cv2.waitKey(0)

show('original', img)

b, g, r = img[6, 40]
b = img[6, 40, 0]
img[6, 40] = (0, 0, 255) # adds a single red pixel
show('one pixel changed', img)

top_left = img[0:50, 0:50]
show('top left', top_left)


# Greyscale
grey_img = cv2.imread(f'{IMG_DIR}/logo.png', cv2.IMREAD_GRAYSCALE)
dims = grey_img.shape
i = grey_img[6, 40]
grey_img[6, 40] = 0
show('grey', grey_img)
