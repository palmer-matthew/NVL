#!/bin/bash

# Running Unit Test in the tests/network folder: Neuron, Network
python3 -m unittest discover -s tests/network 

# Running Unit Test in the tests/parameters
python3 -m unittest discover -s tests/parameters