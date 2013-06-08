import pygame, sys
from pygame.locals import *

from Test import TestState
from Player import Player
from SoundHandler import SoundHandler
from MainMenuState import MainMenuState

class GameHandler:
	_windowSurface = None
	_stateStack = []
	_soundHandler = None

	def __init__(self):
		# set up the window
		self._windowSurface = pygame.display.set_mode((800, 600), 0, 32)
		# create player
		self._player = Player('player1')
		self._stateStack.append(TestState(self._player))
		self._stateStack.append(MainMenuState(self._player))
		self._soundHandler = SoundHandler()

	def loadContent(self):
		self._stateStack[-1].loadContent()

	def update(self):
		self._stateStack[-1].update()

	def draw(self):
		self._stateStack[-1].draw(self._windowSurface)

	@staticmethod
	def pop(self):
		self._stateStack.pop()

	@staticmethod
	def push(self, newState):
		self._stateStack.append(newState)

