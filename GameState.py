import pygame, sys
from pygame.locals import *

from abc import ABCMeta, abstractmethod

class GameState:
	__metaclass__ = ABCMeta

	@abstractmethod
	def loadContent(self, entities):
		pass

	@abstractmethod
	def update(self, keyDown):
		pass

	@abstractmethod
	def draw(self, surface):
		pass
