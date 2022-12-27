import cv2

def cartoon(img):
    # convert image to cv2 image
    # prepare color
    img_color = cv2.pyrDown(cv2.pyrDown(img))
    for _ in range(6):
        img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
    img_color = cv2.pyrUp(cv2.pyrUp(img_color))

    # prepare edges
    img_edges = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img_edges = cv2.adaptiveThreshold(
        cv2.medianBlur(img_edges, 7),
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        2,
    )
    img_edges = cv2.cvtColor(img_edges, cv2.COLOR_GRAY2RGB)

    # combine color and edges
    img = cv2.bitwise_and(img_color, img_edges)
    return img