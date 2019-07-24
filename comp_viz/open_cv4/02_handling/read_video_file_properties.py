import cv2


def decode_fourcc(fourcc):
    '''Decodes the fourcc value to get the chars encoding it'''
    fourcc_int = int(fourcc)
    print(f'Int value of fourcc: {fourcc_int}')
    decoded = ''.join([chr((fourcc_int >> 8 * i) & 0xFF) for i in range(4)])
    print(f'Decoded: {decoded}')
    return decoded

print(f'CV_CAP_PROP_FRAME_WIDTH: {capture.get(cv2.CAP_PROP_FRAME_WIDTH)}')
print(f'CV_CAP_PROP_FRAME_HEIGHT: {capture.get(cv2.CAP_PROP_FRAME_HEIGHT)}')
print(f'CV_CAP_PROP_FPS: {capture.get(cv2.CAP_PROP_FPS)}')
print(f'CV_CAP_PROP_POS_MSEC: {capture.get(cv2.CAP_PROP_POS_MSEC)}')
print(f'CV_CAP_PROP_POS_FRAMES: {capture.get(cv2.CAP_PROP_POS_FRAMES)}')
print(f'CV_CAP_PROP_FOURCC: {capture.get(cv2.CAP_PROP_FOURCC)}')
print(f'CV_CAP_PROP_FRAME_COUNT: {capture.get(cv2.CAP_PROP_FRAME_COUNT)}')
print(f'CV_CAP_PROP_MODE: {capture.get(cv2.CAP_PROP_MODE)}')
print(f'CV_CAP_PROP_BRIGHTNESS: {capture.get(cv2.CAP_PROP_BRIGHTNESS)}')
print(f'CV_CAP_PROP_CONTRAST: {capture.get(cv2.CAP_PROP_CONTRAST)}')
print(f'CV_CAP_PROP_SATURATION: {capture.get(cv2.CAP_PROP_SATURATION)}')
print(f'CV_CAP_PROP_HUE: {capture.get(cv2.CAP_PROP_HUE)}')
print(f'CV_CAP_PROP_GAIN: {capture.get(cv2.CAP_PROP_GAIN)}')
print(f'CV_CAP_PROP_EXPOSURE: {capture.get(cv2.CAP_PROP_EXPOSURE)}')
print(f'CV_CAP_PROP_CONVERT_RGB: {capture.get(cv2.CAP_PROP_CONVERT_RGB)}')
print(f'CV_CAP_PROP_RECTIFICATION: {capture.get(cv2.CAP_PROP_RECTIFICATION)}')
print(f'CV_CAP_PROP_ISO_SPEED: {capture.get(cv2.CAP_PROP_ISO_SPEED)}')
print(f'CV_CAP_PROP_BUFFERSIZE: {capture.get(cv2.CAP_PROP_BUFFERSIZE)}')
