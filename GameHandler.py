import pygame, sys
from pygame.locals import *

from Test import Test

class GameHandler:

	_stateStack = [Test()]

	def __init__(self):
		pass		

	def loadContent(self):
		self._stateStack[-1].loadContent()

	def update(self):
		self._stateStack[-1].update()

	def draw(self):
		self._stateStack[-1].draw()

	@staticmethod
	def pop(self):
		self._stateStack.pop()

	@staticmethod
	def push(self, newState):
		self._stateStack.append(newState)

