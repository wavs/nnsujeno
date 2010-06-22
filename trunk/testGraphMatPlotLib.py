import numpy as np
import pylab as pl
#from scipy.special import jn
from math import *
from physic_cmd import *

times = []
valuesOfError = []
valuesOfDeltaError = []
time = 0

""" Variables """
consigne = 50
error = 0.5
derror = 0

physic = physicSystem(consigne)

while (error > 0.1):
	
	error = physic.getNewError()
	derror = physic.getNewDeltaError(error)
	physic.computeNewPosition(error)
	print error, ":", derror	
	times.append(time)
	time = time + 1
	valuesOfError.append(error)
	valuesOfDeltaError.append(derror)

pl.plot(times, valuesOfError, label='Error')
pl.plot(times, valuesOfDeltaError, label='DeltaError')
pl.title('Evolution de lerreur et de sa derivee')
pl.xlabel("time")
pl.ylabel("")
pl.legend()

pl.show()
