from sugeno_neuron import *
from physic_cmd import *
from pylab import *


## pour le systeme globale
cible = 10.0
seuil = 0.02
current_pos = 0.0
delta_poudre = 0.0

## poudre pour physics module
poudre = 0.0
## pour sujeno_neuronal ou sujeno_normal
# entree de maxErr
maxError = 20
# entree de maxDeltaEr
maxDerr = 20
# entree de maxDeltaPoudre
maxDpoudre = 6


Erreurs = []
deltaErreurs = []
deltaPoudres = []
Positions = []
times = []
time = 0

physics_module = physics(poudre)
command_module = sugeno_neuronal(maxError, maxDerr, maxDpoudre)


while ( (cible - current_pos) >  seuil):
	Positions.append(current_pos)
	deltaPoudres.append(delta_poudre)
	deltaErreurs.append(command_module.funderreur(1))
	Erreurs.append(command_module.funerreur(1))
	times.append(time)
	
	command_module.update(cible - current_pos)  ## update w/ erreur
	delta_poudre = command_module.output()
#	command_module.printFuzzification()
#	print "physics module output %g" %current_pos
#	print "command module output %g" %delta_poudre
	physics_module.update(delta_poudre) ## update w/ deltapoudre
	current_pos = physics_module.output() ## new pos
	time = time + 1
#	print "currentpos = %g" %current_pos
#	print "pause\n"


"""
## print erreurs, positions, delta poudre, delta erreurs en fonction du temps
plot(times, Erreurs, label='Errors')
plot(times, deltaPoudres, label='DeltaPoudres')
plot(times, Positions, label='Positions')
plot(times, deltaErreurs, label='deltaerreurs')
xlim(0,time + 1)
ylim(0, cible + 1)
title('Evolution des: erreurs, delta erreurs, delta poudre et positions')
"""

"""
### print predicat derreur
plot(times, command_module._predicaterreurlt, label='predicat erreur lt')
plot(times, command_module._predicaterreurmt, label='predicat erreur mt')
plot(times, command_module._predicaterreure, label='predicat erreur e')

xlim(0,len(times))
ylim(-0.2,1.4)
title('Evolution des predicats erreur')
## print predicat

"""
### print predicat derreur
plot(times, command_module._predicatderreurlt, label='predicat derreur lt')
plot(times, command_module._predicatderreurmt, label='predicat derreur mt')
plot(times, command_module._predicatderreure, label='predicat derreur e')

xlim(0,len(times)/2) ## techniquement c'est len(times) mais on peut diviser parce ce que l'on veut pour que ce soit plus clair
ylim(-0.2,1.4)
title('Evolution des predicats derreur')
## print predicat
#"""


xlabel("iterations")
ylabel("")
legend()

show()

"""
while ( (cible - current_pos) >  seuil):
	command_module.update(cible - current_pos)  ## update w/ erreur
	print "physics module output %g" %physics_module.output()
	print "command module output %g" %command_module.output()
	physics_module.update(command_module.output()) ## update w/ deltapoudre
	current_pos = physics_module.output() ## new pos
	physics_module.draw()
	print "currentpos = %g" %current_pos
	print "pause\n"

	axvline(10,0,cible)
	physics_module.show()
"""

