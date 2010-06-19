from neuron import *
from arc import *
from math import *

poudre = 2

###### entree

# entree d'erreur
err = 0
# entree de delta erreur
derr = 0

# entree de maxErr
maxError = 2
# entree de maxDeltaEr
maxDerr = 10
# entree de maxDeltaPoudre
maxDpoudre = 10


### neuronne
def fune(x):
	return err
def funde(x):
	return derr
def funMaxE(x):
	return maxError
def funMaxDE(x):
	return maxDpoudre
def funMaxDP(x):
	return maxDpoudre

neuronErreur = neuron(fune)
neuronDErreur = neuron(funde)
neuronMaxE = neuron(funMaxE)
neuronMaxDE = neuron(funMaxDE)
neuronMaxDP = neuron(funMaxDP)

###### fin entree // debut de boucle?

###### fuzzification

# learn how to draw gaussienne

def gaussienne(x,mu,sigma):
	return (1/(sigma*sqrt(2*pi))) * exp( -0.5 * ( pow((x - mu) / (sigma),2 ) ))	
def gaussEqual(x, error): # equal error
	return gaussienne(x,0,0.166666667*error) 
def gaussLT(x, error): # less than error
	return gaussienne(x, -0.5*error,0.166666667*error)
def gaussMT(x, error): #more than error
	return gaussienne(x, 0.5*error,0.166666667*error)



## on a six regles 3 pour le delta erreur et 3 pour le erreur
## neuron erreur
#euronErrorLessThan = neuron()
#neuronErrorEqual = neuron()
#neuronErrorMoreThan = neuron()

## neuron delta erreur
#neuronDErrorLessThan = neuron()
#neuronDErrorEqual = neuron()
#neuronDErrorMoreThan = neuron()

## binding des entrees avec la fuzzification

###### end of fuzzification

###### SUGENO


###### end of SUGENO

###### Defuzzification


###### end of Defuzzification


### multiplication exemple
def funa(x):
	return 4

def funb(x):
	return 3

def funcarre(x):
	return x*x
	
def fununit(x):
	return x

neuronA = neuron(funa)
neuronB = neuron(funb)

neuronAplusBcarre = neuron(funcarre)
neuronAcarre = neuron(funcarre)
neuronBcarre = neuron(funcarre)

neuronA.bindTo(neuronAplusBcarre,1)
neuronB.bindTo(neuronAplusBcarre,1)

neuronA.bindTo(neuronAcarre,1)
neuronB.bindTo(neuronBcarre,1)

neuronMult = neuron(fununit)


neuronAplusBcarre.bindTo(neuronMult, 0.5)
neuronAcarre.bindTo(neuronMult, -0.5)
neuronBcarre.bindTo(neuronMult, -0.5)

#print "neuronA", (neuronA.function)
#print "neuronB", (neuronB.function)
#print "neuronAplusBcarre",(neuronAplusBcarre.function)
#print "neuronAcarre",(neuronAcarre.function)
#print "neuronBcarre",(neuronBcarre.function)
print "NeuronMult",(neuronMult.function)


### fin multiplication exemple