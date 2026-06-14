import numpy as np

class SqueezeNetClassifier:

    def __init__(self):
        pass

    def predict(self, features):

        score = np.median(features)

        probability = 1 / (
            1 + np.exp(-score)
        )

        return probability
