import cv2

def edges(img):
    # perform edge detection
    clr = cv2.Canny(img, 100, 200)
    img = cv2.cvtColor(clr, cv2.COLOR_GRAY2BGR)
    return img