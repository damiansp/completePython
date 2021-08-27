import argparse
import cv2


parser = argparse.ArgumentParser()
parser.add_argument('path_image_input',
                    help='path to imput image to be displayed')
parser.add_argument('path_image_output',
                    help='path for the processed image to be saved')
args = vars(parser.parse_args())

image_input = cv2.imread(args['path_image_input'])
cv2.imshow('loaded', image_input)
grey_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)
cv2.imshow('grey scale', grey_image)
cv2.imwrite(args['path_image_output'], grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
