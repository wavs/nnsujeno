from neuron import *
from node import *
from arc import *

test_primary_node = neuron(node(None,None), 1) # second parameter is fct => 1

print test_primary_node.function
