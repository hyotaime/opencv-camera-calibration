# opencv-camera-calibration

Camera calibration and distortion correction by using opencv

## Checkerboard Image

<img width="450" alt="checkerboard" src="https://github.com/hyotaime/opencv-camera-calibration/assets/109580929/bdfa8996-654f-43a0-9c73-0362247e451a">

## Camera Calibration Input Video
![test_video.gif](test_video.gif)

## Camera Calibration Result

* The number of selected images = 17
* RMS error = `0.7782172075971562`
* Camera Metrix K

  | fx             | fy             | cx             | cy             |
  |----------------|----------------|----------------|----------------|
  | 1.63243490e+03 | 1.63197867e+03 | 7.29840790e+02 | 5.41535124e+02 |
* Distortion Coefficients D

  | k1             | k2              | p1             | p2             | k3             |
  |----------------|-----------------|----------------|----------------|----------------|
  | 2.74755274e-01 | -1.23648857e+00 | 6.93900545e-04 | 2.07391502e-03 | 1.84649263e+00 |

## Distortion Correction Result
![distortion_corrected.gif](distortion_corrected.gif)

## Limitation
* Before the recording, I fix the focus and exposure by tapping the screen so there is no focus/exposure change during the recording
* Test video is taken by an iPhone 13 Pro Max
* Nowadays, smartphone cameras have few distortion, so the result is not so impressive

## References
* [mint-lab/cv-tutorial](https://github.com/mint-lab/cv_tutorial)
* [mint-lab/3dv_tutorial](https://github.com/mint-lab/3dv_tutorial)
