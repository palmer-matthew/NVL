import unittest
from src.network.neuron import Neuron

class TestNeuron(unittest.TestCase):

    def testConstctA(self):
        test = Neuron(0.5)
        self.assertEqual(test.getActivation(), 0.50, "Should be 0.50")
        
    def testConstrctB(self):
        test = Neuron(0.5)
        self.assertEqual(test.getBias(), 0.05, "Should be 0.05")

if __name__ == "__main__":
    unittest.main()