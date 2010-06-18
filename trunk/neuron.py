class neuron(object):
	def __init__(self, node, function):
		self._node = node
		self._function = function
	def blabla(self):
		print self._node,self._function
	def getn(self):
		return self._node
	def setn(self, value):
		self._node = value
	def deln(self):
		del self._node
	node = property(getn, setn, deln, "I'm the 'x' property.")
