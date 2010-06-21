from math_neuron import *

class sugeno_neuron(object):
	def __init__(self, maxErreur, maxDerreur, maxDpoudre):
		self._maxErreur = maxErreur
		self._maxDerreur = maxDerreur
		self._maxDpoudre = maxDpoudre
		self._erreur = 0
		self._derreur = 0
	def update(erreur):
		self._derreur = self_.erreur - erreur
		self._erreur = erreur
	def funerreur(x):
		return self._erreur
	def funderreur(x):
		return self._derreur
	def initInput(self):
		self.neuronErreur = neuron(funerreur) ## fun1 est defini dans math_neuron
		self.neuronDErreur = neuron(funderreur) ## generalement toutes les fun sont dans math_neu
		self.neuronMaxE = neuron(fun1)
		self.neuronMaxDE = neuron(fun1)
		self.neuronMaxDP = neuron(fun1)