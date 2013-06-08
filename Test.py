import pygame, sys
from pygame.locals import *
from GameState import GameState

from abc import ABCMeta, abstractmethod

class TestState(GameState):
	_player = None

	def __init__(self, player):
		self._player = player
	
	def loadContent(self):
		pass

	def update(self):
		pass

	def draw(self, windowSurface):
		# draw the white background onto the surface
		windowSurface.fill((255,255,255))
		# draw the player
		self._player.draw(windowSurface)
		# draw the window onto the screen
		pygame.display.update()