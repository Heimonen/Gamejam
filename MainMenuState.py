import pygame, sys, math, time
from pygame.locals import *

from GameState import GameState
from SoundHandler import SoundHandler
from Test import TestState

class MainMenuState(GameState):

	_title = None
	_enter = None
	_surface = None

	def __init__(self, player):
		pass
	
	def loadContent(self, entities):
		SoundHandler.playSong('Title.wav')
		self._title = pygame.transform.scale2x(pygame.image.load('gamejam.png'))
		self._enter = pygame.image.load('enter.png')
		pygame.time.Clock() 


	def update(self, keyDown):
		if K_RETURN in keyDown:
			GameHandler.push(TestState(self._surface))

	def draw(self, windowSurface):
		self._surface = windowSurface
		# draw the black background onto the surface
		windowSurface.fill((0,0,0))
		# draw the title image
		scale = math.sin(pygame.time.get_ticks() / float(1000)) / 2 + 1
		enterScale = math.sin(pygame.time.get_ticks() / float(300)) / 2 + 1
		print scale
		newSurface = pygame.transform.scale(self._title,(int(self._title.get_width() * scale), \
		 int(self._title.get_height() * scale)))
		windowSurface.blit(newSurface, ((windowSurface.get_width() - newSurface.get_width()) / 2, 20))
		# Draw press enter
		if enterScale < 1:
			windowSurface.blit(self._enter, ((windowSurface.get_width() - self._enter.get_width()) / 2, \
		 	 windowSurface.get_height() - (windowSurface.get_height() - self._enter.get_height()) / 3))
		# draw the window onto the screen
		pygame.display.update()

	def resize(surface, size):
		scale = size / float(max(surface.get_rect().size))
		return pygame.transform.rotozoom(surface, 0, scale)
