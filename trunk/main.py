from neuron import *
from arc import *
from math import *
from math_neuron import *
from sugeno_neuron import *
from physic_cmd import *

cible = 10.0
seuil = 0.1
current_pos = 0.0
poudre = 10.0
# entree de maxErr
maxError = 4
# entree de maxDeltaEr
maxDerr = 10
# entree de maxDeltaPoudre
maxDpoudre = 10


physics_module = physics(0)
command_module = sugeno_neuronal(maxError, maxDerr, maxDpoudre)

print "commande module test", command_module.output()

while 0 & ( (cible - current_pos) >  seuil):
 	command_module.update(cible - current_pos)
	physics_module.update(command_module.output())
	current_pos = physics_module.output()
###### debut entree

# entree d'erreur
err = 0.5
# entree de delta erreur
derr = 0

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
## A signifie le poid et Y signifie fonction de contribution?=

## neuron less than less than == llthan
nLTLTA = multiplication(neuronGELT, neuronGDELT)
nY1 = neuron(fununit)
neuronGELT.bindTo(nY1, 0.5)
neuronGDELT.bindTo(nY1, 0.5)
nLTLTY = multiplication(nY1, neuronmuDPmaxLLT)
## neuron less than equal == lthan
nLTEA = multiplication(neuronGELT, neuronGDEE)
nY2 = neuron(fununit)
neuronGELT.bindTo(nY2, 0.5)
neuronGDEE.bindTo(nY2, 0.5)
nLTEY = multiplication(nY2, neuronmuDPmaxLT)
## neuron less than more than == equal
nLTMTA = multiplication(neuronGELT, neuronGDEMT)
nY3 = neuron(fununit)
neuronGELT.bindTo(nY3, 0.5)
neuronGDEMT.bindTo(nY3, 0.5)
nLTMTY = multiplication(nY3, neuronmuDPmaxE)
## neuron equal less than == lthan
nELTA = multiplication(neuronGEE, neuronGDELT)
nY4 = neuron(fununit)
neuronGEE.bindTo(nY4, 0.5)
neuronGDELT.bindTo(nY4, 0.5)
nELTY = multiplication(nY4, neuronmuDPmaxLT)
## neuron equal equal == equal
nEEA = multiplication(neuronGEE, neuronGDEE)
nY5 = neuron(fununit)
neuronGEE.bindTo(nY5, 0.5)
neuronGDEE.bindTo(nY5, 0.5)
nEEY = multiplication(nY5, neuronmuDPmaxE)
## neuron equal more than = mthan
nEMTA = multiplication(neuronGEE, neuronGDEMT)
nY6 = neuron(fununit)
neuronGEE.bindTo(nY6, 0.5)
neuronGDEMT.bindTo(nY6, 0.5)
nEMTY = multiplication(nY6, neuronmuDPmaxMT)
## neuron more than less than == equal
nMTLTA = multiplication(neuronGEMT, neuronGDELT)
nY7 = neuron(fununit)
neuronGEMT.bindTo(nY7, 0.5)
neuronGDELT.bindTo(nY7, 0.5)
nMTLTY = multiplication(nY7, neuronmuDPmaxE)
## neuron more than equal == morthan
nMTEA = multiplication(neuronGEMT, neuronGDEE)
nY8 = neuron(fununit)
neuronGEMT.bindTo(nY8, 0.5)
neuronGDEE.bindTo(nY8, 0.5)
nMTEY = multiplication(nY8, neuronmuDPmaxMT)
## neuron more than more than == mmthan
nMTMTA = multiplication(neuronGEMT, neuronGDEMT)
nY9 = neuron(fununit)
neuronGEMT.bindTo(nY9, 0.5)
neuronGDEMT.bindTo(nY9, 0.5)
nMTMTY = multiplication(nY9, neuronmuDPmaxMMT)
###### end of SUGENO

###### Defuzzification

#doing sum of all A
neuronsumofA = neuron(fununit)

nMTMTA.bindTo(neuronsumofA,1)
nMTEA.bindTo(neuronsumofA,1)
nMTLTA.bindTo(neuronsumofA,1)

nEMTA.bindTo(neuronsumofA,1)
nEEA.bindTo(neuronsumofA,1)
nELTA.bindTo(neuronsumofA,1)

nLTLTA.bindTo(neuronsumofA,1)
nLTEA.bindTo(neuronsumofA,1)
nLTMTA.bindTo(neuronsumofA,1)
# doing for each 9 of the sugeno result ai*yi / the previous sum
## meaning of those are obvious (look into the multiplication)
ndefuzz1 = division(multiplication(nMTMTA,nMTMTY), neuronsumofA)
ndefuzz2 = division(multiplication(nMTEA,nMTEY), neuronsumofA)
ndefuzz3 = division(multiplication(nMTLTA,nMTLTY), neuronsumofA)

ndefuzz4 = division(multiplication(nEMTA,nEMTY), neuronsumofA)
ndefuzz5 = division(multiplication(nEEA,nEEY), neuronsumofA)
ndefuzz6 = division(multiplication(nELTA,nELTY), neuronsumofA)

ndefuzz7 = division(multiplication(nLTLTA,nLTLTY), neuronsumofA)
ndefuzz8 = division(multiplication(nLTEA,nLTEY), neuronsumofA)
ndefuzz9 = division(multiplication(nLTMTA,nLTMTY), neuronsumofA)

## doing graph for those function to

# doing all the sum of the previous 9 item
neuronDefuzzOut = neuron(fununit)

ndefuzz1.bindTo(neuronDefuzzOut, 1)
ndefuzz2.bindTo(neuronDefuzzOut, 1)
ndefuzz3.bindTo(neuronDefuzzOut, 1)

ndefuzz4.bindTo(neuronDefuzzOut, 1)
ndefuzz5.bindTo(neuronDefuzzOut, 1)
ndefuzz6.bindTo(neuronDefuzzOut, 1)

ndefuzz7.bindTo(neuronDefuzzOut, 1)
ndefuzz8.bindTo(neuronDefuzzOut, 1)
ndefuzz9.bindTo(neuronDefuzzOut, 1)

## it's our output -->> deltapoudre we want
# neuronDefuzzOut.function is our output <== Deltapoudre
print "neurondefuzzout",neuronDefuzzOut.function

###### end of Defuzzification


### multiplication exemple
def funa(x):
	return 10
def funb(x):
	return 4.0
neuronA = neuron(funa)
neuronB = neuron(funb)

neuronMult = division(neuronA, neuronB)

print "NeuronMult",(neuronMult.function)

### fin multiplication exemple