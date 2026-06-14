import cv2
import numpy as np

class MultitextonFeatures:

    def __init__(self):
        pass

    def extract(self, image):

        gray = image.copy()

        gx = cv2.Sobel(
            gray,
            cv2.CV_64F,
            1,
            0,
            ksize=3
        )

        gy = cv2.Sobel(
            gray,
            cv2.CV_64F,
            0,
            1,
            ksize=3
        )

        magnitude = np.sqrt(
            gx**2 + gy**2
        )

        mean_texture = np.mean(magnitude)

        std_texture = np.std(magnitude)

        max_texture = np.max(magnitude)

        return np.array([
            mean_texture,
            std_texture,
            max_texture
        ])
