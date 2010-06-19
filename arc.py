class arc(object):
	def __init__(self, weight, beginNeurone, endNeurone):
		self._weight = weight
		self._beginNeurone = beginNeurone
		self._endNeurone = endNeurone
	
	def getweight(self):
		return self._weight
	def setweight(self, value):
		self._weight = value
	def delweight(self):
		del self._weight
	weight = property(getweight, setweight, delweight, "I'm the 'weight' property.")
	
	def getbeginNeurone(self):
		return self._beginNeurone
	def setbeginNeurone(self, value):
		self._beginNeurone = value
	def delbeginNeurone(self):
		del self._beginNeurone
	beginNeurone = property(getbeginNeurone, setbeginNeurone, delbeginNeurone, "I'm the 'beginNeurone' property.")
	
	def getendNeurone(self):
		return self._endNeurone
	def setendNeurone(self, value):
		self._endNeurone = value
	def delendNeurone(self):
		del self._endNeurone
	endNeurone = property(getendNeurone, setendNeurone, delendNeurone, "I'm the 'endNeurone' property.")