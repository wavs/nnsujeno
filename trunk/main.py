from sugeno_neuron import *
from physic_cmd import *
from pylab import *
from math_neuron import *


## pour le systeme globale
cible = 10.0
seuil = 0.2
current_pos = 0.0
delta_poudre = 0.0

## poudre pour physics module
poudre = 0.0
## pour sujeno_neuronal ou sujeno_normal
# entree de maxErr
maxError = cible*2
# entree de maxDeltaEr
maxDerr = cible*2
# entree de maxDeltaPoudre
maxDpoudre = 10

maxEapprentissage = 6

Erreurs = []
deltaErreurs = []
deltaPoudres = []
ErreursLearn = []
DerreurLearn = []
Positions = []
times = []
time = 0

physics_module = physics(poudre)
command_module = sugeno_neuronal(maxError, maxDerr, maxDpoudre, maxEapprentissage, cible)


while (( abs(cible - current_pos) >  seuil) and (time < 200)):

	
	ErreursLearn.append(command_module._neuronLearnGaussienne.function)
	delta_poudre = command_module.output()
	command_module.update(cible - current_pos)  ## update w/ erreur


#	command_module.printFuzzification()
#	print "physics module output %g" %current_pos
#	print "command module output %g" %delta_poudre
	Positions.append(current_pos)
	deltaPoudres.append(delta_poudre)
	deltaErreurs.append(command_module.funderreur(1))
	Erreurs.append(command_module.funerreur(1))

	DerreurLearn.append(command_module._neuronLearnGaussienne.function - command_module.funerreur(1))
	physics_module.update(delta_poudre) ## update w/ deltapoudre
	current_pos = physics_module.output() ## new pos
	

	times.append(time)
#	print "cible - current_pos" ,(cible - current_pos)
#	command_module.printInput()
	time = time + 1

## si l'on n'aime pas la fin des courbes, on commente les append suivant
#"""
ErreursLearn.append(command_module._neuronLearnGaussienne.function)
Positions.append(current_pos)
deltaPoudres.append(delta_poudre)
deltaErreurs.append(command_module.funderreur(1))
Erreurs.append(command_module.funerreur(1))
DerreurLearn.append(command_module._neuronLearnGaussienne.function - command_module.funerreur(1))
command_module.update(cible - current_pos)
times.append(time)
#"""

#"""
## print erreurs, positions, delta poudre, delta erreurs en fonction du temps
plot(times, Erreurs, label='Errors')
plot(times, deltaPoudres, label='DeltaPoudres')
plot(times, Positions, label='Positions')
plot(times, deltaErreurs, label='deltaerreurs')
xlim(0,time + 1)
ylim(-cible, cible + 1)
title('Evolution des: erreurs, delta erreurs, delta poudre et positions')
#"""

"""
## print erreurs, positions, delta poudre, delta erreurs et apprentisage en fonction du temps
plot(times, Erreurs, label='Errors', linewidth=2)
plot(times, deltaPoudres, label='DeltaPoudres', linewidth=2)
plot(times, Positions, label='Positions', linewidth=2)
plot(times, deltaErreurs, label='deltaerreurs', linewidth=2)
plot(times, ErreursLearn, label='ErreursLearn', linewidth=2)
plot(times, DerreurLearn, label='DerreurLearn', linewidth=2)
xlim(0,time + 1)
ylim(-cible, cible + 1)
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

"""
### print predicat derreur
plot(times, command_module._predicatderreurlt, label='predicat derreur lt')
plot(times, command_module._predicatderreurmt, label='predicat derreur mt')
plot(times, command_module._predicatderreure, label='predicat derreur e')

xlim(0,len(times)) ## techniquement c'est len(times) mais on peut diviser parce ce que l'on veut pour que ce soit plus clair
ylim(-0.2,1.4)
title('Evolution des predicats derreur')
## print predicat
"""

"""
### print predicat y1 - y9
plot(times, command_module._Y1, label="MT MT", linewidth=2)
plot(times, command_module._Y2, label="MT E", linewidth=2)
plot(times, command_module._Y3, label="MT LT", linewidth=2)

plot(times, command_module._Y4, label="E MT", linewidth=2)
plot(times, command_module._Y5, label="E E", linewidth=2)
plot(times, command_module._Y6, label="E LT", linewidth=2)

plot(times, command_module._Y7, label="LT MT", linewidth=2)
plot(times, command_module._Y8, label="LT E", linewidth=2)
plot(times, command_module._Y9, label="LT LT", linewidth=2)

xlim(0,len(times))
ylim(0,3)
title("predicat y1--y9")
## fin predicat Y1 -- Y9
"""

"""
### print predicat Ay1 - Ay9
plot(times, command_module._AY1, label="MT MT", linewidth=2)
plot(times, command_module._AY2, label="MT E", linewidth=2)
plot(times, command_module._AY3, label="MT LT", linewidth=2)

plot(times, command_module._AY4, label="E MT", linewidth=2)
plot(times, command_module._AY5, label="E E", linewidth=2)
plot(times, command_module._AY6, label="E LT", linewidth=2)

plot(times, command_module._AY7, label="LT MT", linewidth=2)
plot(times, command_module._AY8, label="LT E", linewidth=2)
plot(times, command_module._AY9, label="LT LT", linewidth=2)

xlim(0,len(times))
ylim(0,2.2)
title("contribution unitaire, centre de gravite a1y1/sum(ai)--a9y9/sum(ai)")
## fin predicat Y1 -- Y9
"""

"""
## graphique pour la derivee de la quantitee de poudre

## ca correspond aux sorties ai*yi/moyemme
## qu'on somme pour faire correspondre les regles

plot(times, command_module._MMT, label="MMT", linewidth=2)
plot(times, command_module._MT, label="MMT", linewidth=2)
plot(times, command_module._E, label="E", linewidth=2)
plot(times, command_module._LT, label="LT", linewidth=2)
plot(times, command_module._LLT, label="LLT", linewidth=2)

xlim(0, len(times))
ylim(0, 2)
title("graphique pour la derivee de la quantitee de poudre")

## fin du graphique pour la derivee de la quantitee de poudre
"""



xlabel("iterations")
ylabel("")
legend()

show()


## old loop
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

