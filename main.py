from sugeno_neuron import *
from physic_cmd import *


## pour le systeme globale
cible = 10.0
seuil = 0.01
current_pos = 0.0

## poudre pour physics module
poudre = 0.0
## pour sujeno_neuronal ou sujeno_normal
# entree de maxErr
maxError = 20
# entree de maxDeltaEr
maxDerr = 20
# entree de maxDeltaPoudre
maxDpoudre = 7.69


physics_module = physics(poudre)
command_module = sugeno_neuronal(maxError, maxDerr, maxDpoudre)

while ( (cible - current_pos) >  seuil):
	command_module.update(cible - current_pos)  ## update w/ erreur
	print "physics module output %g" %physics_module.output()
	print "command module output %g" %command_module.output()
	physics_module.update(command_module.output()) ## update w/ deltapoudre
	current_pos = physics_module.output() ## new pos
	physics_module.draw()
	
	print "currentpos = %g" %current_pos
	print "pause\n"	
#axvline(cible,0,cible)
physics_module.show()