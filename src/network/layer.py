from .neuron import Neuron
from random import uniform
# import numpy as np

"""
"""
class Layer(object):

    """
    """
    #Edit to use **kwargs [Named Dictionary of Arguments]
    def __init__(self, num:int, activation:function) -> None:
        self.activation = activation
        self.num_neurons = num
        self.layer  = [Neuron() for i in range(num)]
    
    def getActivations(self) -> list:
        return [i.getActivation() for i in self.layer]
    
    def getBiases(self) -> list:
        return [i.getBias() for i in self.layer]



class InputLayer(Layer):
    
    def __init__(num, activation,):
        super.__init__()

    def changeInput(self, values) -> None:
        for i, val in enumerate(self.layer):
            val.setActivation(values[i])

class OutputLayer(Layer):
    
    def __init__(num, activation,):
        super.__init__()


class HiddenLayer(Layer):

    def __init__(self, num:int, activation:list, prev:int) -> None:
        super.__init__(num, activation)
        self.prev = prev 
        self.init_weights()
    
    def init_weights(self) -> None:
        ## Possible Improvement is to use a numpy matrix
        self.weights = []
        for i in range(self.num):
            self.weights.append([round(uniform(0,1), 2) for i in range(self.prev)])

    def forwardProp(self, pactivations:list) -> None:
        ## Possible Improvement is to use np.dot
        for i, node in enumerate(self.layer):
            lcomb = 0
            for j, weight in enumerate(self.weights[i]):
                lcomb += weight * pactivations[j]
            result =  self.activation(lcomb + node.getBias())
            node.setActivation(result)

    def backwardProp(self, **args):
        pass