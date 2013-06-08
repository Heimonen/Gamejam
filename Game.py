import pygame, sys
from pygame.locals import *
from Entity import Entity
from Player import Player

from GameHandler import GameHandler
from LevelPainter import LevelPainter


class Game:
	fpsClock = pygame.time.Clock()
	_gameHandler = GameHandler()

	def __init__(self):
		pass

	def run(self):
		self.loadContent()
		# Game Loop
		while(True):
			self.update()
			self.draw()
			self.fpsClock.tick(60)

	def update(self):
		self._gameHandler.handleInput()
		self._gameHandler.update()

	def draw(self):
		self._gameHandler.draw()

	def init(self):
		pass

	def loadContent(self):
		self._gameHandler.loadContent()
		pygame.init()
		stuff = LevelPainter("hej")

if  __name__ =='__main__':
	game = Game()
	game.run()
