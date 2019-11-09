# Press c on keyboard to save current frame
if cv2.waitKey(20) & 0xFF == ord('c'):
    frame_name = f'camera_frame_{format(frame_index)}.png'
    grey_frame_name = f'greyscale_{frame_name}'
    cv2.imwrite(frame_name, frame)
    cv2.imwrite(grey_frame_name, grey_frame)
    frame_index += 1
