from tensorflow.keras.layers import *
from tensorflow.keras.models import Model

from attention_block import attention_block

def build_munet(input_shape=(256,256,1)):

    inputs = Input(input_shape)

    c1 = Conv2D(
        32,
        (3,3),
        activation='relu',
        padding='same'
    )(inputs)

    c1 = attention_block(c1)

    p1 = MaxPooling2D((2,2))(c1)

    c2 = Conv2D(
        64,
        (3,3),
        activation='relu',
        padding='same'
    )(p1)

    c2 = attention_block(c2)

    u1 = UpSampling2D((2,2))(c2)

    outputs = Conv2D(
        1,
        (1,1),
        activation='sigmoid'
    )(u1)

    model = Model(inputs, outputs)

    return model
