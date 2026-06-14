import cv2

def enhance_image(image):

    image = cv2.equalizeHist(image)

    return image
