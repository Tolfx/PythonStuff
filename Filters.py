import cv2
import numpy as np

def dummy(value):
    pass

identity_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
gaussian_kernel1 = cv2.getGaussianKernel(3, 0)
gaussian_kernel2 = cv2.getGaussianKernel(5, 0)
box_kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.float32) / 9.0

kernels = [identity_kernel, sharpen_kernel, gaussian_kernel1, gaussian_kernel2, box_kernel]

color_original = cv2.imread('TX.png')
gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('Image manipulation')
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, len(kernels)-1, dummy)
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

count = 1
while True:
    grayscale = cv2.getTrackbarPos('grayscale', 'app')
    contrast = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')
    kernel_idx = cv2.getTrackbarPos('filter', 'app')

    color_modified = cv2.filter2D(color_original, -1, kernels[kernel_idx])
    gray_modified = cv2.filter2D(gray_original, -1, kernels[kernel_idx])
    
    color_modified = cv2.addWeighted(color_modified, contrast, np.zeros_like(color_original), 0, brightness - 50)
    gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros_like(gray_original), 0, brightness - 50)
    
    key = cv2.waitKey(100)
    if key == ord('q'):
        break
    elif key == ord('s'):
        if grayscale == 0:
            cv2.imwrite('output-{}.png'.format(count), color_modified)
        else:
            cv2.imwrite('output-{}.png'.format(count), gray_modified)
        count += 1
    
    if grayscale == 0:
        cv2.imshow('app', color_modified)
    else:
        cv2.imshow('app', gray_modified)

cv2.destroyAllWindows()