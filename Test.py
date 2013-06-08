import pygame, sys
from pygame.locals import *

from abc import ABCMeta, abstractmethod

class Test:
	windowSurface = None

	def loadContent(self):
		# set up the window
		self.windowSurface = pygame.display.set_mode((1024, 768), 0, 32)

	def update(self):
		pass

	def draw(self):
		# draw the white background onto the surface
		self.windowSurface.fill((255,255,255))
		# draw a green polygon onto the surface
		pygame.draw.polygon(self.windowSurface, (0,255,0), ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
		# draw the window onto the screen
		pygame.display.update()