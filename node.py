class node(object):
	def __init__(self, inArc, outArc):
		self._inArc = inArc
		self._outArc = outArc
		
	def getInArc(self):
		return self._inArc
	def setInArc(self, value):
		self._inArc = value
	def delInArc(self):
		del self._inArc
	inArc = property(getInArc, setInArc, delInArc, "I'm the 'InArc' property.")
	
	def getOutArc(self):
		return self._outArc
	def setOutArc(self, value):
		self._outArc = value
	def delOutArc(self):
		del self._outArc
	outArc = property(getOutArc, setOutArc, delOutArc, "I'm the 'OutArc' property.")