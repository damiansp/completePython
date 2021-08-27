import argparse
import cv2


parser = argparse.ArgumentParser()
parser.add_argument(
    'index_camera', help='index of the camera to read from', type=int)
args = parser.parse_args()
capture = cv2.VideoCapture(args.index_camera)
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)
print(f'Width: {frame_width}\nHeight: {frame_height}\nFPS: {fps}')
if not capture.isOpened():
    print('Error opening the camera')

# Read until video completed
while capture.isOpened():
    # Capture frame by frame from camera
    ret, frame = capture.read()
    if ret:
        cv2.imshow('Input frame from the camera', frame)
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grey scale input camera', grey_frame)
        if cv2.waitKey(20) and 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
    
