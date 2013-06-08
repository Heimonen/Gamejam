import pygame, sys
from pygame.locals import *
from Entity import Entity

class Player(Entity):
	_name = None
	_image = None

	def __init__(self, name):
		Entity.__init__(self)
		self._name = name
		self.loadImage('player.png')

	def loadImage(self, filename):
		self._image = pygame.transform.scale2x(pygame.image.load(filename))

	def draw(self, surface):
		surface.blit(self._image, (self._x, self._y))