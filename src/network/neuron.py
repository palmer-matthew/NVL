import random

"""
    This class represents a singular node/Neuron in a Neural Network
"""
class Neuron(object):

    """
        The constructor will initialize the weight of a Neuron to be a given weight or if no weight is given
        then it will generate a random weight in the range [0,1) or [0,1]
    """
    def __init__(self, weight=round(random.uniform(0,1),2)) -> None:
        if type(weight) != float and type(weight) != int:
            self.weight = round(random.uniform(0,1),2) 
        else:
            self.weight = weight

    """
        This function returns the internal weight of a Neuron
    """
    def getWeight(self) -> int:
        return self.weight
    
    """
        This function modifies the internal weight of a Neuron
    """
    def setWeight(self, weight) -> None:
        self.weight = weight