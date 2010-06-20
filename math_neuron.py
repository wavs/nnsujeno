from neuron import *
from math import *

# return x*x
def funcarre(x):
	return x*x

# return 1/x
def fundiv(x):
	return 1.0/x

# return x
def fununit(x):
	return x

# return 1
def fun1(x):
	return 1

# exponent
def fun0(x):
	return 0.0

def funexp(x):
	return exp(x)

def funsixth(x):
	return x/6.0

def funminhalf(x):
	return -x/2.0

def funhalf(x):
	return x/2.0

def funthird(x):
	return x/3.0

def funminthird(x):
	return -x/3.0

def funmintwothird(x):
	return -2.0*x/3.0

def funtwothird(x):
	return 2.0*x/3.0

# neurona mult neuronb
def multiplication(neurona, neuronb):
	neuronAplusBcarre = neuron(funcarre)
	neuronAcarre = neuron(funcarre)
	neuronBcarre = neuron(funcarre)
	neurona.bindTo(neuronAplusBcarre,1)
	neuronb.bindTo(neuronAplusBcarre,1)
	neurona.bindTo(neuronAcarre,1)
	neuronb.bindTo(neuronBcarre,1)
	neuronMult = neuron(fununit)
	neuronAplusBcarre.bindTo(neuronMult, 0.5)
	neuronAcarre.bindTo(neuronMult, -0.5)
	neuronBcarre.bindTo(neuronMult, -0.5)
	return neuronMult


# neurona div neuronx
def division(neurona,neuronx):
	neuronb = neuron(fundiv)
	neuronx.bindTo(neuronb,1)
	neuronAplusBcarre = neuron(funcarre)
	neuronAcarre = neuron(funcarre)
	neuronBcarre = neuron(funcarre)
	neurona.bindTo(neuronAplusBcarre,1)
	neuronb.bindTo(neuronAplusBcarre,1)
	neurona.bindTo(neuronAcarre,1)
	neuronb.bindTo(neuronBcarre,1)
	neuronDiv = neuron(fununit)
	neuronAplusBcarre.bindTo(neuronDiv, 0.5)
	neuronAcarre.bindTo(neuronDiv, -0.5)
	neuronBcarre.bindTo(neuronDiv, -0.5)
	return neuronDiv


def gaussienne(neuronx, neuronmu, neuronsigma):
	neuronnumerateur = neuron(funcarre)
	# binding x et mu
	neuronx.bindTo(neuronnumerateur, 1)
	neuronmu.bindTo(neuronnumerateur, -1)
	## sigma carre
	neuronsigmacarre = neuron(funcarre)
	neuronsigma.bindTo(neuronsigmacarre, 1)
	
	# neuron division
	
	neurondivision = division(neuronnumerateur, neuronsigmacarre)
	neuronOutGaussienne = neuron(funexp)
	neurondivision.bindTo(neuronOutGaussienne, -1.0/2)
	
	return neuronOutGaussienne
