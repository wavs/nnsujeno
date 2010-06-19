from neuron import *
from node import *
from arc import *

a = 3
b = 4

test_primary_node = neuron(node(None,None), a) # second parameter is fct => 1
test_secondary_node = neuron(node(None,None), b)

arc1 = arc(1, test_primary_node.node, test_secondary_node.node)


print test_primary_node.function
print test_secondary_node.function

