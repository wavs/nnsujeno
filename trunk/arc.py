class arc(object):
	def __init__(self, weight, beginNode, endNode):
		self._weight = weight
		self._beginNode = beginNode
		self._endNode = endNode
	
	def getweight(self):
		return self.weight
	def setweight(self, value):
		self._weight = value
	def delweight(self):
		del self._weight
	weight = property(getweight, setweight, delweight, "I'm the 'weight' property.")
	
	def getbeginNode(self):
		return self._beginNode
	def setbeginNode(self, value):
		self._beginNode = value
	def delbeginNode(self):
		del self._beginNode
	beginNode = property(getbeginNode, setbeginNode, delbeginNode, "I'm the 'beginNode' property.")
	
	def getendNode(self):
		return self._endNode
	def setendNode(self, value):
		self._endNode = value
	def delendNode(self):
		del self._endNode
	endNode = property(getendNode, setendNode, delendNode, "I'm the 'endNode' property.")