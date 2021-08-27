import argparse

import cv2


parser = argparse.ArgumentParser()
parser.add_argument('output_video_path', help='path to the video file to write')
args = parser.parse_args()

# Create a VideoCapture obj and pass 0 as arg to read from the camera
capture = cv2.VideoCapture(0)
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D') # platform dependent!
out_grey = cv2.VideoWriter(
    args.output_video_path, fourcc, int(fps), (int(width), int(height)), False)
# last arg = True for color

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out_grey.write(grey_frame)
        # show frame until 'q' pressed (not necessary for writing)
        cv2.imshow('grey', grey_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
out_grey.release()
cv2.destroyAllWindows()

                                                                
