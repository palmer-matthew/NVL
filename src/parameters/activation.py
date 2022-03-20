"""
    This file houses all the activation functions that can be used by a layer
"""
import numpy as np

"""
    This function represents the reLU activation function. For values less than 0, it will return 0.
    For values greater than 0, it return the value given.
"""
def reLU(input) -> float:
    return 0 if input < 0 else round(float(input), 2)

"""
    This function represents the sigmoid activation function. [Explanation of Domain]
"""
def sigmoid(input) -> float:
    return 1.0 / (1.0 + np.exp(-input)) 