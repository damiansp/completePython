import cv2


# Play backwards
frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1
capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
ret, frame = capture.read()
frame_index -= 1
