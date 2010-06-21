from sugeno_neuron import *
from physic_cmd import *


## pour le systeme globale
cible = 10.0
seuil = 0.1
current_pos = 0.0

## poudre pour physics module
poudre = 10.0
## pour sujeno_neuronal ou sujeno_normal
# entree de maxErr
maxError = 4
# entree de maxDeltaEr
maxDerr = 10
# entree de maxDeltaPoudre
maxDpoudre = 10


physics_module = physics(poudre)
command_module = sugeno_neuronal(maxError, maxDerr, maxDpoudre)

print "commande module test", command_module.output()

while 0 & ( (cible - current_pos) >  seuil):
 	command_module.update(cible - current_pos) ## update w/ erreur
	physics_module.update(command_module.output()) ## update w/ deltapoudre
	current_pos = physics_module.output() ## new pos