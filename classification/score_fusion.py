import numpy as np

class ScoreFusion:

    def __init__(self):
        pass

    def tanh_mad_normalization(
        self,
        score
    ):

        return 0.5 * (
            np.tanh(score)
            + 1
        )

    def adaptive_weight(
        self,
        score
    ):

        return score / (
            score + 1e-8
        )

    def fuse(
        self,
        linknet_score,
        squeezenet_score
    ):

        l_score = self.tanh_mad_normalization(
            linknet_score
        )

        s_score = self.tanh_mad_normalization(
            squeezenet_score
        )

        w1 = self.adaptive_weight(
            l_score
        )

        w2 = self.adaptive_weight(
            s_score
        )

        fused_score = (
            w1 * l_score +
            w2 * s_score
        ) / (
            w1 + w2
        )

        return fused_score
