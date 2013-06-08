import pygame, sys
from pygame.locals import *

class Entity:

	_x = 0
	_y = 0

	def __init__(self):
		pass

	def setPosition(self, x, y):
		self._x = x
		self._y = y

	def update(self):
		pass

	def draw(self):
		pass