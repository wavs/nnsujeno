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
		x = self._vo*cos(self._theta)*t
		y = (self._vo*cos(self._theta)*t)/(-0.5*self._g*t*t)
		plot(x, y, linewidth=10.0)
		xlim(xmin, ymax)
		ylim(ymin, ymax)
		print 'xmin', xmin, 'xmax', xmax
		xlabel('x')
		ylabel('y')
		title('About as simple as it gets, folks')
		grid(True)
		show()