import numpy as np

class LinkNetClassifier:

    def __init__(self):
        pass

    def predict(self, features):

        score = np.mean(features)

        probability = 1 / (
            1 + np.exp(-score)
        )

        return probability
