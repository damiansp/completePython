#!/usr/bin/env python3
# use
#    python3 -m pydoc -w test
# to generate documentation
'''Test script to play with OpenCV and Python'''
import cv2

def show_message():
    return 'this function returns a message'


def load_image(path):
    '''loads the image given by <path>'''
    return cv2.imread(path)


def show_image(image):
    '''shows an <image> until key is pressed'''
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def convert_to_greyscale(image):
    '''converts a BGR image to greyscale'''
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def write_image_to_disk(path, image):
    '''write <image> to <path>'''
    cv2.imwrite(path, image)


if __name__ == '__main__':
    print('hello_opencv.py being run directly')
    print(show_message())
    bgr_image = load_image('images/logo.png')
    show_image(bgr_image)
    grey_image = convert_to_greyscale(bgr_image)
    show_image(grey_image)
    write_image_to_disk('images/grey_logo.png', grey_image)
else:
    print('hello_opencv.py imported into another module')
