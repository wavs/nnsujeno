from neuron import *
from arc import *
from math import *
from math_neuron import *

poudre = 2

###### debut entree

# entree d'erreur
err = 0.5
# entree de delta erreur
derr = 0

# entree de maxErr
maxError = 4
# entree de maxDeltaEr
maxDerr = 10
# entree de maxDeltaPoudre
maxDpoudre = 10


### neuronne
def funerreur(x):
	return err
def funderreur(x):
	return derr

## les valeurs max ERROR MAXDPOUDRE ET MAX DERROR Doivent etre des poids

neuronErreur = neuron(funerreur) ## fun1 est defini dans math_neuron
neuronDErreur = neuron(funderreur) ## generalement toutes les fun sont dans math_neu
neuronMaxE = neuron(fun1)
neuronMaxDE = neuron(fun1)
neuronMaxDP = neuron(fun1)

###### fin entree // debut de boucle?

###### fuzzification
## pour errmax et derrmax sigma = 1/6 Errmax ou Derrmax et mu = -1/2 0 ou 1/2
## de errmax ou derrmax
######## valeur gaussienne errmax
#neuron errmax sigma |less than| equal | more than
neuronsigmaEmax = neuron(funsixth)
neuronMaxE.bindTo(neuronsigmaEmax, maxError)
#neuron errmax mu less than
neuronmuEmaxLT = neuron(funminhalf)
neuronMaxE.bindTo(neuronmuEmaxLT, maxError)
#neuron errmax mu equal
neuronmuEmaxE = neuron(fun0)
neuronMaxE.bindTo(neuronmuEmaxE, maxError)
#neuron errmax mu more than
neuronmuEmaxMT = neuron(funhalf)
neuronMaxE.bindTo(neuronmuEmaxMT, maxError)

# neuron gaussienne ERREUR LT
neuronGELT = gaussienne(neuronErreur, neuronmuEmaxLT, neuronsigmaEmax)
# neuron gaussienne ERREUR EQUAL
neuronGEE = gaussienne(neuronErreur, neuronmuEmaxE, neuronsigmaEmax)
# neuron gaussienne ERREUR MT
neuronGEMT = gaussienne(neuronErreur, neuronmuEmaxMT, neuronsigmaEmax)

### valeur gaussienne deltaerrmax
#neuron derrmax sigma |less than| more than | equal
neuronsigmaDEmax = neuron(funsixth)
neuronMaxDE.bindTo(neuronsigmaDEmax, maxDerr)
#neuron derrmax mu less than
neuronmuDEmaxLT = neuron(funminhalf)
neuronMaxDE.bindTo(neuronmuDEmaxLT, maxDerr)
#neuron derrmax mu equal
neuronmuDEmaxE = neuron(fun0)
neuronMaxDE.bindTo(neuronmuDEmaxE, maxDerr)
#neuron derrmax mu more than
neuronmuDEmaxMT = neuron(funhalf)
neuronMaxDE.bindTo(neuronmuDEmaxMT, maxDerr)

# neuron gaussienne DERREUR LT
neuronGDELT = gaussienne(neuronDErreur, neuronmuDEmaxLT, neuronsigmaDEmax)
# neuron gaussienne DERREUR EQUAL
neuronGDEE = gaussienne(neuronDErreur, neuronmuDEmaxE, neuronsigmaDEmax)
# neuron gaussienne DERREUR MT
neuronGDEMT = gaussienne(neuronDErreur, neuronmuDEmaxMT, neuronsigmaDEmax)

### valeur gaussienne deltapoudremax
#### on a besoin que du mu
#### sigma = 1/9 de deltaerrmax ==> on a 5 mu different
#### (-2/3)DP (-1/3)DP 0*DP (1/3)DP (2/3)DP

#neuronmu dpoudremax mu less less than
neuronmuDPmaxLLT = neuron(funmintwothird)
neuronMaxDP.bindTo(neuronmuDPmaxLLT, maxDpoudre)
#neuronmu dpoudremax mu less than
neuronmuDPmaxLT = neuron(funminthird)
neuronMaxDP.bindTo(neuronmuDPmaxLT, maxDpoudre)
#neuronmu dpoudremax mu equal
neuronmuDPmaxE = neuron(fun0)
neuronMaxDP.bindTo(neuronmuDPmaxE, maxDpoudre)
#neuronmu dpoudremax mu more than
neuronmuDPmaxMT = neuron(funthird)
neuronMaxDP.bindTo(neuronmuDPmaxMT, maxDpoudre)
#neuronmu dpoudremax mu more more than
neuronmuDPmaxMMT = neuron(funtwothird)
neuronMaxDP.bindTo(neuronmuDPmaxMMT, maxDpoudre)

###### end of fuzzification

###### SUGENO


###### end of SUGENO

###### Defuzzification


###### end of Defuzzification


### multiplication exemple
def funa(x):
	return 10
def funb(x):
	return 4.0
neuronA = neuron(funa)
neuronB = neuron(funb)

neuronMult = division(neuronA, neuronB)

#print "neuronA", (neuronA.function)
#print "neuronB", (neuronB.function)
#print "neuronAplusBcarre",(neuronAplusBcarre.function)
#print "neuronAcarre",(neuronAcarre.function)
#print "neuronBcarre",(neuronBcarre.function)
print "NeuronMult",(neuronMult.function)


### fin multiplication exemple