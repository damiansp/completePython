kernel_averaging_5x5 = np.ones((5, 5), np.float32) / 25
smooth_image_f2D = cv2.filter2D(image, -1, kernel_averageing_5x5)
