

import cv2

def rotate(img, angle):
    rows, cols, _ = img.shape
    M = cv2.getRotationMatrix2D(
        (cols / 2, rows / 2), angle, 1)
    return cv2.warpAffine(img, M, (cols, rows))
