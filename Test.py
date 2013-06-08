import pygame, sys
from pygame.locals import *
from GameState import GameState
from Player import Player

from abc import ABCMeta, abstractmethod

class TestState(GameState):
	_entities = []
	_surface = None

	def __init__(self, surface):
		self._surface = surface
	
	def loadContent(self, entities):
		self._entities = entities
		for entity in entities:
			if isinstance (entity, Player):
				entity.setPosition(100, 100)

	def update(self, keyDown):
		for entity in self._entities:
			entity.update(keyDown)

	def draw(self, windowSurface):
		# draw the white background onto the surface
		windowSurface.fill((255,255,255))
		
		for entity in self._entities:
			entity.draw(self._surface)
		# draw the window onto the screen
		pygame.display.update()