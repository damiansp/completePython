import argparse

import cv2


parser = argparse.ArgumentParser()
parser.add_argument('output_video_path', help='path to the video file to write')
args = parser.parse_args()
print(args)
print(args.output_video_path)

# Create a VideoCapture obj and pass 0 as arg to read from the camera
capture = cv2.VideoCapture(0)
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D') # platform dependent!
out_grey = cv2.VideoWriter(
    args.output_video_path, fourcc, int(fps), (int(width), int(height)), False)
# last arg = True for color
