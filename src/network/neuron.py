import random

"""
    This class represents a singular node/Neuron in a Neural Network
"""
class Neuron(object):

    """
        The constructor will initialize the activation of a Neuron to be a given activation or if no activation is given
        then it will generate a random activation in the range [0,1) or [0,1]
    """
    def __init__(self, activation:float=round(random.uniform(0,1),2)) -> None:
        if type(activation) != float and type(activation) != int:
            self.activation = round(random.uniform(0,1),2) 
        else:
            self.activation = activation
        self.bias = 0.05

    """
        This function returns the internal activation of a Neuron
    """
    def getActivation(self) -> float:
        return self.activation
    
    """
        This function modifies the internal activation of a Neuron
    """
    def setActivation(self, activation:float) -> None:
        self.activation = activation
    
    """
        This function returns the internal bias of a Neuron
    """
    def getBias(self) -> float:
        return self.bias
    
    """
        This function modifies the internal bias of a Neuron
    """
    def setBias(self, bias:float) -> None:
        self.bias = bias