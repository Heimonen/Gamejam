import pygame, sys
from pygame.locals import *
from Entity import Entity

class Player(Entity):
	_UP = K_w
	_DOWN = K_s
	_LEFT = K_a
	_RIGHT = K_d

	_name = None
	_images = []
	_speed = 1
	_animationState = 0

	def __init__(self, name):
		Entity.__init__(self)
		self._name = name
		self.addImage('player1.png')
		self.addImage('player2.png')

	def addImage(self, filename):
		self._images.append(pygame.transform.scale2x(pygame.image.load(filename)))

	def update(self, keyDown):
		if self._RIGHT in keyDown and keyDown[self._RIGHT]:
			self._x = self._x + self._speed
		elif self._LEFT in keyDown and keyDown[self._LEFT]:
			self._x = self._x - self._speed
		elif self._UP in keyDown and keyDown[self._UP]:
			self._animationState = 1
		elif self._DOWN in keyDown and keyDown[self._DOWN]:
			self._animationState = 0

	def draw(self, surface):
		if self._animationState == 0:
			surface.blit(self._images[0], (self._x, self._y))
		elif self._animationState == 1:
			surface.blit(self._images[1], (self._x, self._y))