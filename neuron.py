class neuron(object):
	def __init__(self, node, function):
		self._node = node
		self._function = function

	def getf(self):
		return self._function
	def setf(self, value):
		self._function = value
	def delf(self):
		del self._function
	function = property(getf, setf, delf, "I'm the 'node' property.")


	def getn(self):
		return self._node
	def setn(self, value):
		self._node = value
	def deln(self):
		del self._node
	node = property(getn, setn, deln, "I'm the 'node' property.")
