from sugeno_neuron import *
from physic_cmd import *


## pour le systeme globale
cible = 10.0
seuil = 0.1
current_pos = 0.0

## poudre pour physics module
poudre = 0.0
## pour sujeno_neuronal ou sujeno_normal
# entree de maxErr
maxError = 20
# entree de maxDeltaEr
maxDerr = 20
# entree de maxDeltaPoudre
maxDpoudre = 4


physics_module = physics(poudre)
command_module = sugeno_neuronal(maxError, maxDerr, maxDpoudre)

command_module.update(cible - current_pos)
command_module.printInput()
command_module.printFuzzification()
command_module.printSujenoRules()
print command_module.output()
physics_module.update(command_module.output()) ## update w/ deltapoudre
#physics_module.draw()



#physics_module.update(5)
#physics_module.draw()
#physics_module.update(5)
#physics_module.draw()


while 0 & ( (cible - current_pos) >  seuil):
 	command_module.update(cible - current_pos) ## update w/ erreur
	
	physics_module.update(command_module.output()) ## update w/ deltapoudre
	physics_module.draw()
	current_pos = physics_module.output() ## new pos
#physics_module.show()