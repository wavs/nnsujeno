from math import *

from pylab import *
from math import *

xmin = 0
xmax = 50
ymin = 0
ymax = 50

class physics(object):
	def __init__(self, poudre):
		self._poudre = poudre
		self._theta = 45.0
		self._g = 10.0
		self._xo = 0.
		self._yo = 0.
		self._increment = 0.01
		self._v0 = self._poudre * 2.0
	def update(self, deltapoudre):
		self._poudre = self._poudre + deltapoudre
		self._v0 = self._poudre * 2.0
	def output(self):
		# v^2 /g
		return (self._v0*self._v0/ self._g)
	def posx(self,t):
		return (self._xo + (self._v0*cos(45.0)*t))
	def posy(self,t):
		return (self._yo + (self._v0*sin(45.0)*t) - ((self._g*t*t)/2.0))
	def draw(self):
		time = 0
		valuesofy = []
		valuesofx = []
		y = 0
		x = 0
		while (y >= 0.0):
			y = self.posy(time)
			x = self.posx(time)
			time = time + self._increment
			valuesofy.append(y)
			valuesofx.append(x)

		plot(valuesofx, valuesofy, label='boulet')
		title('Evolution du boulet au cours du temps')
		xlabel("x")
		ylabel("y")
		legend()
		ylim(-0.0, ((x + 1) / 2))
		xlim(-0.0, x + 1)
	def show(self):
		show()



class physicSystem(object):
	def __init__(self, consigne):
		""" Position et vitesse d'origine """
		self._x0 = 0
		self._y0 = 0
		self._v0 = 0
		
		""" Constantes """
		self._gravity = 9.64
		self._theta = 45
		
		self._omega = 0
		self._p = 0
		self._consigne = consigne
		self._olderror = 0
		self._coefError = 0.1

	def vx(self, p):
		return (p * cos(self._theta))
		
	def vy(self, p):
		return (p * sin(self._theta))

	def posx(self, t):
		return ( (-0.5 * self._gravity * t * t * self._omega) + (self.vx(self._p) * t) + self._x0 )

	def posy(self, t):
		return ( (-0.5 * self._gravity * t * t) + (self.vy(self._p) * t) + self._y0 )
		
	def distance(self, x, y, theta):
		return ( sqrt((x * x) + (y * y)) )
		
	def powder(self, x, y, theta):
		return ( self.distance(x,y,theta) / 2 )
		
	def impact(self, p):
		return ( self.posx( (2 * p * sin(self._theta)) / self._gravity ) )
		
	def getNewError(self):
		return ( self._consigne - self.impact(self._p) )
		
	def getNewDeltaError(self, error):
		return ( error - self._olderror )
		
	def computeNewPosition(self, error):
		self._p = self._p + (self._coefError * error)