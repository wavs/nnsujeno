from arc import *

class neuron(object):
	def __init__(self, function):
		self._function = function
		self._inArcs = []
		self._outArcs = []

	def getInArcs(self):
		return self._inArcs
	def setInArcs(self, value):
		self._inArcs = value
	def delInArcs(self):
		del self._inArcs

	inArcs = property(getInArcs, setInArcs, delInArcs, "I'm the 'InArcs' property.")

	def getOutArcs(self):
		return self._outArcs
	def setOutArcs(self, value):
		self._outArcs = value
	def delOutArcs(self):
		del self._outArcs
	outArcs = property(getOutArcs, setOutArcs, delOutArcs, "I'm the 'OutArcs' property.")


	def getf(self):
		sumNodeWeight = 0
		for i in range(len(self._inArcs)):
		   sumNodeWeight += self._inArcs[i].weight * self._inArcs[i].beginNeurone.function
		return self._function(sumNodeWeight)
	def setf(self, value):
		self._function = value
	def delf(self):
		del self._function
	function = property(getf, setf, delf, "I'm the 'node' property.")
	
	
	def bindTo(self, neurone, weight):
		tempArc = arc(weight, self, neurone)
		neurone.inArcs += [tempArc]
		self._outArcs += [tempArc]

