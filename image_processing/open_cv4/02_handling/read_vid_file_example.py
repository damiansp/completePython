parser = argparse.ArgumentParser()
parser.add_argument('video_path', help='path to the video file')
args = parser.parse_args()
capture = cv2.VideoCapture(args.video_path)
    
