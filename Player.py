import pygame, sys
from pygame.locals import *
from Entity import Entity

class Player(Entity):
	_UP = K_w
	_DOWN = K_s
	_LEFT = K_a
	_RIGHT = K_d

	_name = None
	_image = None
	_speed = 1

	def __init__(self, name):
		Entity.__init__(self)
		self._name = name
		self.loadImage('player.png')

	def loadImage(self, filename):
		self._image = pygame.transform.scale2x(pygame.image.load(filename))

	def update(self, keyDown):
		if self._RIGHT in keyDown and keyDown[self._RIGHT] == True:
			self._x = self._x + self._speed
		elif self._LEFT in keyDown and keyDown[self._LEFT] == True:
			self._x = self._x - self._speed

	def draw(self, surface):
		surface.blit(self._image, (self._x, self._y))