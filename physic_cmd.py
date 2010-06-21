from math import *

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

		

"""
from pylab import *
from math import *

xmin = -50
xmax = 50
ymin = -50
ymax = 50

class physics(object):
	def __init__(self, poudre):
		self._poudre = poudre
		self._theta = 45.0
		self._g = 10.0
		self._xo = 0.
		self._yo = 0.
		self._vo = poudre * 5.0
	def update(self, deltapoudre):
		self._poudre = self._poudre + deltapoudre
	def output(self):
		# v^2 /g
		return (self._vo*self._vo/ self._g)
	def draw(self):
		t = 1

		for t in range(100):
			if t > 0:
				x = self._vo*cos(self._theta)*t
				y = (self._vo*cos(self._theta)*t)/(-0.5*self._g*t*t)
				xlim(xmin, ymax)
				ylim(ymin, ymax)
				plot(x, y, linewidth=1.0)

		print 'xmin', xmin, 'xmax', xmax
		xlabel('x')
		ylabel('y')
		title('About as simple as it gets, folks')
		grid(True)
		show()
"""