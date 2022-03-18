import unittest
import src.parameters.activation as act

class TestActivation(unittest.TestCase):
    
    def testreLU(self):
        self.assertEqual(act.reLU(-1), 0, "reLU: -1 Should be 0")

if __name__ == "__main__":
    unittest.main()