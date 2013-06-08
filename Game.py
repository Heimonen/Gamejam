import pygame, sys
from pygame.locals import *
from Entity import Entity
from Player import Player

from GameHandler import GameHandler


class Game:
	fpsClock = pygame.time.Clock()
	_gameHandler = GameHandler()

	def __init__(self):
		pass

	def run(self):
		self.loadContent()
		# Game Loop
		while(True):
			self.checkInput()
			self.update()
			self.draw()
			self.fpsClock.tick(60)

	def checkInput(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

	def update(self):
		self._gameHandler.update()

	def draw(self):
		self._gameHandler.draw()

	def init(self):
		pass

	def loadContent(self):
		self._gameHandler.loadContent()
		pygame.init()

if  __name__ =='__main__':
	game = Game()
	game.run()