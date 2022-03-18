from .neuron import Neuron

"""
"""
class Layer(object):

    """
    """
    def __init__(self, num, activation) -> None:
        self.activation = activation
        self.num_neurons = num
        self.layer  = [Neuron() for i in range(num)]