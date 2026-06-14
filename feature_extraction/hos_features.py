import cv2
import numpy as np

class HOSFeatures:

    def __init__(self):
        pass

    def extract(self, silhouette):

        height, width = silhouette.shape[:2]

        area = np.sum(silhouette > 0)

        perimeter = cv2.arcLength(
            cv2.findContours(
                silhouette,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE
            )[0][0],
            True
        ) if area > 0 else 0

        aspect_ratio = width / (height + 1e-8)

        feature_vector = np.array([
            area,
            perimeter,
            aspect_ratio
        ])

        return feature_vector
