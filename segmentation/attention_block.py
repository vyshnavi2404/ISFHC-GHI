from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Multiply

def attention_block(x):

    attention = Conv2D(
        1,
        (1,1),
        activation='sigmoid'
    )(x)

    output = Multiply()([x, attention])

    return output
