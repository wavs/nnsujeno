from math_neuron import *

class sugeno_neuronal(object):
	def __init__(self, maxErreur, maxDerreur, maxDpoudre):
		self._maxError = maxErreur
		self._maxDerr = maxDerreur
		self._maxDpoudre = maxDpoudre
		self._erreur = 0.5
		self._derreur = 0.0
		self.initInput()
		self.fuzzification()
		self.sujeno_rules()
		self.defuzzification()
	def update(self, erreur):
		self._derreur = self._erreur - erreur
		self._erreur = erreur
	def funerreur(self,x):
		return self._erreur
	def funderreur(self,x):
		return self._derreur
	def initInput(self):
		## les valeurs max ERROR MAXDPOUDRE ET MAX DERROR Doivent etre des poids
		self._neuronErreur = neuron(self.funerreur) ## fun1 est defini dans math_neuron
		self._neuronDErreur = neuron(self.funderreur) ## generalement toutes les fun sont dans math_neu
		self._neuronMaxE = neuron(fun1)
		self._neuronMaxDE = neuron(fun1)
		self._neuronMaxDP = neuron(fun1)
	def fuzzification(self):
		###### fuzzification
		## pour errmax et derrmax sigma = 1/6 Errmax ou Derrmax et mu = -1/2 0 ou 1/2
		## de errmax ou derrmax
		######## valeur gaussienne errmax
		#neuron errmax sigma |less than| equal | more than
		self._neuronsigmaEmax = neuron(funsixth)
		self._neuronMaxE.bindTo(self._neuronsigmaEmax, self._maxError)
		#neuron errmax mu less than
		self._neuronmuEmaxLT = neuron(funminhalf)
		self._neuronMaxE.bindTo(self._neuronmuEmaxLT, self._maxError)
		#neuron errmax mu equal
		self._neuronmuEmaxE = neuron(fun0)
		self._neuronMaxE.bindTo(self._neuronmuEmaxE, self._maxError)
		#neuron errmax mu more than
		self._neuronmuEmaxMT = neuron(funhalf)
		self._neuronMaxE.bindTo(self._neuronmuEmaxMT, self._maxError)

		# neuron gaussienne ERREUR LT
		self._neuronGELT = gaussienne(self._neuronErreur, self._neuronmuEmaxLT, self._neuronsigmaEmax)
		# neuron gaussienne ERREUR EQUAL
		self._neuronGEE = gaussienne(self._neuronErreur, self._neuronmuEmaxE, self._neuronsigmaEmax)
		# neuron gaussienne ERREUR MT
		self._neuronGEMT = gaussienne(self._neuronErreur, self._neuronmuEmaxMT, self._neuronsigmaEmax)

		### valeur gaussienne deltaerrmax
		#neuron derrmax sigma |less than| more than | equal
		self._neuronsigmaDEmax = neuron(funsixth)
		self._neuronMaxDE.bindTo(self._neuronsigmaDEmax, self._maxDerr)
		#neuron derrmax mu less than
		self._neuronmuDEmaxLT = neuron(funminhalf)
		self._neuronMaxDE.bindTo(self._neuronmuDEmaxLT, self._maxDerr)
		#neuron derrmax mu equal
		self._neuronmuDEmaxE = neuron(fun0)
		self._neuronMaxDE.bindTo(self._neuronmuDEmaxE, self._maxDerr)
		#neuron derrmax mu more than
		self._neuronmuDEmaxMT = neuron(funhalf)
		self._neuronMaxDE.bindTo(self._neuronmuDEmaxMT, self._maxDerr)

		# neuron gaussienne DERREUR LT
		self._neuronGDELT = gaussienne(self._neuronDErreur, self._neuronmuDEmaxLT, self._neuronsigmaDEmax)
		# neuron gaussienne DERREUR EQUAL
		self._neuronGDEE = gaussienne(self._neuronDErreur, self._neuronmuDEmaxE, self._neuronsigmaDEmax)
		# neuron gaussienne DERREUR MT
		self._neuronGDEMT = gaussienne(self._neuronDErreur, self._neuronmuDEmaxMT, self._neuronsigmaDEmax)

		### valeur gaussienne deltapoudremax
		#### on a besoin que du mu
		#### sigma = 1/9 de deltaerrmax ==> on a 5 mu different
		#### (-2/3)DP (-1/3)DP 0*DP (1/3)DP (2/3)DP

		#neuronmu dpoudremax mu less less than
		self._neuronmuDPmaxLLT = neuron(funmintwothird)
		self._neuronMaxDP.bindTo(self._neuronmuDPmaxLLT, self._maxDpoudre)
		#neuronmu dpoudremax mu less than
		self._neuronmuDPmaxLT = neuron(funminthird)
		self._neuronMaxDP.bindTo(self._neuronmuDPmaxLT, self._maxDpoudre)
		#neuronmu dpoudremax mu equal
		self._neuronmuDPmaxE = neuron(fun0)
		self._neuronMaxDP.bindTo(self._neuronmuDPmaxE, self._maxDpoudre)
		#neuronmu dpoudremax mu more than
		self._neuronmuDPmaxMT = neuron(funthird)
		self._neuronMaxDP.bindTo(self._neuronmuDPmaxMT, self._maxDpoudre)
		#neuronmu dpoudremax mu more more than
		self._neuronmuDPmaxMMT = neuron(funtwothird)
		self._neuronMaxDP.bindTo(self._neuronmuDPmaxMMT, self._maxDpoudre)
		###### end of fuzzification
	def sujeno_rules(self):
		## A signifie le poid et Y signifie fonction de contribution?=

		## neuron less than less than == llthan
		self._nLTLTA = multiplication(self._neuronGELT, self._neuronGDELT)
		nY1 = neuron(fununit)
		self._neuronGELT.bindTo(nY1, 0.5)
		self._neuronGDELT.bindTo(nY1, 0.5)
		self._nLTLTY = multiplication(nY1, self._neuronmuDPmaxLLT)
		## neuron less than equal == lthan
		self._nLTEA = multiplication(self._neuronGELT, self._neuronGDEE)
		nY2 = neuron(fununit)
		self._neuronGELT.bindTo(nY2, 0.5)
		self._neuronGDEE.bindTo(nY2, 0.5)
		self._nLTEY = multiplication(nY2, self._neuronmuDPmaxLT)
		## neuron less than more than == equal
		self._nLTMTA = multiplication(self._neuronGELT, self._neuronGDEMT)
		nY3 = neuron(fununit)
		self._neuronGELT.bindTo(nY3, 0.5)
		self._neuronGDEMT.bindTo(nY3, 0.5)
		self._nLTMTY = multiplication(nY3, self._neuronmuDPmaxE)
		## neuron equal less than == lthan
		self._nELTA = multiplication(self._neuronGEE, self._neuronGDELT)
		nY4 = neuron(fununit)
		self._neuronGEE.bindTo(nY4, 0.5)
		self._neuronGDELT.bindTo(nY4, 0.5)
		self._nELTY = multiplication(nY4, self._neuronmuDPmaxLT)
		## neuron equal equal == equal
		self._nEEA = multiplication(self._neuronGEE, self._neuronGDEE)
		nY5 = neuron(fununit)
		self._neuronGEE.bindTo(nY5, 0.5)
		self._neuronGDEE.bindTo(nY5, 0.5)
		self._nEEY = multiplication(nY5, self._neuronmuDPmaxE)
		## neuron equal more than = mthan
		self._nEMTA = multiplication(self._neuronGEE, self._neuronGDEMT)
		nY6 = neuron(fununit)
		self._neuronGEE.bindTo(nY6, 0.5)
		self._neuronGDEMT.bindTo(nY6, 0.5)
		self._nEMTY = multiplication(nY6, self._neuronmuDPmaxMT)
		## neuron more than less than == equal
		self._nMTLTA = multiplication(self._neuronGEMT, self._neuronGDELT)
		nY7 = neuron(fununit)
		self._neuronGEMT.bindTo(nY7, 0.5)
		self._neuronGDELT.bindTo(nY7, 0.5)
		self._nMTLTY = multiplication(nY7, self._neuronmuDPmaxE)
		## neuron more than equal == morthan
		self._nMTEA = multiplication(self._neuronGEMT, self._neuronGDEE)
		nY8 = neuron(fununit)
		self._neuronGEMT.bindTo(nY8, 0.5)
		self._neuronGDEE.bindTo(nY8, 0.5)
		self._nMTEY = multiplication(nY8, self._neuronmuDPmaxMT)
		## neuron more than more than == mmthan
		self._nMTMTA = multiplication(self._neuronGEMT, self._neuronGDEMT)
		nY9 = neuron(fununit)
		self._neuronGEMT.bindTo(nY9, 0.5)
		self._neuronGDEMT.bindTo(nY9, 0.5)
		self._nMTMTY = multiplication(nY9, self._neuronmuDPmaxMMT)
		###### end of SUGENO rules
	def defuzzification(self):
		#doing sum of all A
		self._neuronsumofA = neuron(fununit)

		self._nMTMTA.bindTo(self._neuronsumofA,1)
		self._nMTEA.bindTo(self._neuronsumofA,1)
		self._nMTLTA.bindTo(self._neuronsumofA,1)

		self._nEMTA.bindTo(self._neuronsumofA,1)
		self._nEEA.bindTo(self._neuronsumofA,1)
		self._nELTA.bindTo(self._neuronsumofA,1)

		self._nLTLTA.bindTo(self._neuronsumofA,1)
		self._nLTEA.bindTo(self._neuronsumofA,1)
		self._nLTMTA.bindTo(self._neuronsumofA,1)
		# doing for each 9 of the sugeno result ai*yi / the previous sum
		## meaning of those are obvious (look into the multiplication)
		self._ndefuzz1 = division(multiplication(self._nMTMTA,self._nMTMTY), self._neuronsumofA)
		self._ndefuzz2 = division(multiplication(self._nMTEA,self._nMTEY), self._neuronsumofA)
		self._ndefuzz3 = division(multiplication(self._nMTLTA,self._nMTLTY), self._neuronsumofA)

		self._ndefuzz4 = division(multiplication(self._nEMTA,self._nEMTY), self._neuronsumofA)
		self._ndefuzz5 = division(multiplication(self._nEEA,self._nEEY), self._neuronsumofA)
		self._ndefuzz6 = division(multiplication(self._nELTA,self._nELTY), self._neuronsumofA)

		self._ndefuzz7 = division(multiplication(self._nLTLTA,self._nLTLTY), self._neuronsumofA)
		self._ndefuzz8 = division(multiplication(self._nLTEA,self._nLTEY), self._neuronsumofA)
		self._ndefuzz9 = division(multiplication(self._nLTMTA,self._nLTMTY), self._neuronsumofA)

		## doing graph for those function to

		# doing all the sum of the previous 9 item
		self._neuronDefuzzOut = neuron(fununit)

		self._ndefuzz1.bindTo(self._neuronDefuzzOut, 1)
		self._ndefuzz2.bindTo(self._neuronDefuzzOut, 1)
		self._ndefuzz3.bindTo(self._neuronDefuzzOut, 1)

		self._ndefuzz4.bindTo(self._neuronDefuzzOut, 1)
		self._ndefuzz5.bindTo(self._neuronDefuzzOut, 1)
		self._ndefuzz6.bindTo(self._neuronDefuzzOut, 1)

		self._ndefuzz7.bindTo(self._neuronDefuzzOut, 1)
		self._ndefuzz8.bindTo(self._neuronDefuzzOut, 1)
		self._ndefuzz9.bindTo(self._neuronDefuzzOut, 1)
		## it's our output -->> deltapoudre we want
		# neuronDefuzzOut.function is our output <== Deltapoudre
	def output(self):
		## we reset neuron 	self._neuronErreur = neuron(self.funerreur) 
		##	self._neuronDErreur = neuron(self.funderreur)
		self._neuronDErreur.function = self.funderreur
		self._neuronErreur.function = self.funerreur
		return self._neuronDefuzzOut.function