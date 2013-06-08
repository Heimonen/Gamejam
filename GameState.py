import pygame, sys
from pygame.locals import *

from abc import ABCMeta, abstractmethod

class GameState:
	__metaclass__ = ABCMeta

	@abstractmethod
	def loadContent(self):
		pass

	@abstractmethod
	def update(self):
		pass

	@abstractmethod
	def draw(self):
		pass
