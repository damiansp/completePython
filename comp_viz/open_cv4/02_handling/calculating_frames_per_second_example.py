# Read vid til done or 'q' pressed
while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        processing_start = time.time()
        # processing code here...
        processing_time = time.time() - processing_start
        print(f'FPS: {1. / processing_time}')
    else:
        break

