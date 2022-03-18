import unittest
from src.network.neuron import Neuron

class TestNeuron(unittest.TestCase):

    def test(self):
        test = Neuron(0.5)
        self.assertEqual(test.getWeight(), 0.50, "Should be 0.50")

if __name__ == "__main__":
    unittest.main()