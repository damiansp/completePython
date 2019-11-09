import cv2

from hello_opencv import (
    convert_to_greyscale, load_image, show_message, write_image_to_disk)


def test_show_message():
    '''Test for show_message'''
    print("testing show_message")
    assert show_message() == "this function returns a message"


def test_load_image():
    """Test for load_image"""
    print("testing load_image")
    bgr_image = load_image("images/logo.png")
    assert bgr_image is not None


def test_write_image_to_disk():
    """Test for write_image_to_disk"""
    print("testing write_image_to_disk")
    bgr_image = load_image("images/logo.png")
    write_image_to_disk("images/temp.png", bgr_image)
    temp = load_image("images/temp.png")
    assert bgr_image.shape == temp.shape
    difference = cv2.subtract(bgr_image, temp)
    b, g, r = cv2.split(difference)
    assert cv2.countNonZero(b) == 0\
        and cv2.countNonZero(g) == 0\
        and cv2.countNonZero(r) == 0


def test_convert_to_greyscale():
    """Test for write_image_to_disk"""
    print("testing test_convert_to_grayscale")
    bgr_image = load_image("images/logo.png")
    grey_image = convert_to_greyscale(bgr_image)
    bgr_height, bgr_width, bgr_channels = bgr_image.shape
    grey_height, grey_width = grey_image.shape
    assert bgr_height == grey_height and bgr_width == grey_width
