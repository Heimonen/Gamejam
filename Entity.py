import pygame, sys
from pygame.locals import *

class Entity:

	_x = 0
	_y = 0
	_name = ""

	def __init__(self):
		pass

	def setPosition(self, x, y):
		self._x = x
		self._y = y

	def update(self, keyDown):
		pass

	def draw(self, surface):
		pass

	def setName(self, name):
		self._name = name

	def toString(self):
		return self._name