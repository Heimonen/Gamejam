import pygame, sys
from pygame.locals import *

from Test import TestState
from Player import Player
from LevelPainter import LevelPainter

class GameHandler:

	_windowSurface = None
	_stateStack = []
	_entities = []
	
	_keyDown = {}

	def __init__(self):
		# set up the window
		self._windowSurface = pygame.display.set_mode((800, 600), 0, 32)
		# create player
		self._player = Player('player1')
		self._entities.append(self._player)
		self._stateStack.append(TestState(self._windowSurface))

		lp = LevelPainter("level0.txt", self._entities)

	def loadContent(self):
		self._stateStack[-1].loadContent(self._entities)

	def update(self):
		self._stateStack[-1].update(self._keyDown)

	def draw(self):
		self._stateStack[-1].draw(self._windowSurface)

	def handleInput(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				self._keyDown[event.key] = True
			elif event.type == KEYUP:
				self._keyDown[event.key] = False

	@staticmethod
	def pop(self):
		self._stateStack.pop()

	@staticmethod
	def push(self, newState):
		self._stateStack.append(newState)
