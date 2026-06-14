import cv2
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis

class ColorFeatures:

    def __init__(self):
        pass

    def extract(self, image):

        pixels = image.flatten()

        mean_val = np.mean(pixels)

        std_val = np.std(pixels)

        skewness = skew(pixels)

        kurt = kurtosis(pixels)

        entropy = -np.sum(
            np.histogram(
                pixels,
                bins=256
            )[0] + 1e-8
        )

        return np.array([
            mean_val,
            std_val,
            skewness,
            kurt,
            entropy
        ])
