import numpy as np
import cv2 as cv

# The given video and calibration data
input_file = './test_video.mov'
K = np.array([[1.63243490e+03, 0, 7.29840790e+02],
              [0, 1.63197867e+03, 5.41535124e+02],
              [0, 0, 1]])

dist_coeff = np.array([2.74755274e-01, -1.23648857e+00,  6.93900545e-04,  2.07391502e-03, 1.84649263e+00])
# Open a video
video = cv.VideoCapture(input_file)
assert video.isOpened(), 'Cannot read the given input, ' + input_file

fourcc = cv.VideoWriter.fourcc(*'mp4v')
out = cv.VideoWriter('distortion_corrected.mp4', fourcc, 20.0, (int(video.get(3)), int(video.get(4))))

# Run distortion correction
show_rectify = True
map1, map2 = None, None
while True:
    # Read an image from the video
    valid, img = video.read()
    if not valid:
        break

    # Rectify geometric distortion (Alternative: cv.undistort())
    info = "Original"
    if show_rectify:
        if map1 is None or map2 is None:
            map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]),
                                                    cv.CV_32FC1)
        img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
        info = "Rectified"
    cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

    # Show the image and process the key event
    cv.imshow("Distortion Correction", img)
    # Save the distortion corrected video
    out.write(img)

    key = cv.waitKey(10)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27:  # ESC
        break
    elif key == ord('\t'):
        show_rectify = not show_rectify

video.release()
cv.destroyAllWindows()
