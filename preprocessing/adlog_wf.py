import cv2
import numpy as np

class AdLOG_WF:

    def __init__(self):
        pass

    def gaussian_smoothing(self, image):
        return cv2.GaussianBlur(image, (5,5), 0)

    def laplacian_enhancement(self, image):
        lap = cv2.Laplacian(image, cv2.CV_64F)
        return cv2.convertScaleAbs(lap)

    def adaptive_filter(self, image):
        smooth = self.gaussian_smoothing(image)
        edge = self.laplacian_enhancement(smooth)

        enhanced = cv2.addWeighted(
            smooth,
            0.7,
            edge,
            0.3,
            0
        )

        return enhanced

    def process(self, image):
        return self.adaptive_filter(image)
