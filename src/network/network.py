from .layer import *
from ..parameters.activation import *

class NeuralNetwork():

    layer_map = {
        "I": InputLayer,
        "H": HiddenLayer,
        "O": OutputLayer
    }
    
    def __init__(self, num:int, layers:list, nodes:list, activations:list) -> None:
        self.num = num
        self.layers = []
        for i in range(self.num):
            self.layers.append(self.layer_map[layers[i]](nodes[i], activations[i]))

    def forwardPropogation():
        pass

    def train(self):
        pass

    def evaluate(self):
        pass

    def predict(self):
        pass