import pygame, sys
from pygame.locals import *
from Entity import Entity
from Player import Player

class Game:
	windowSurface = None
	fpsClock = pygame.time.Clock()
	player = None

	def run(self):
		self.init()
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
		pass

	def draw(self):
		# draw the white background onto the surface
		self.windowSurface.fill((255,255,255))
		# draw the player
		self.player.draw(self.windowSurface)
		# draw the window onto the screen
		pygame.display.update()

	def init(self):
		pygame.init()
		# set up the window
		self.windowSurface = pygame.display.set_mode((1024, 768), 0, 32)

	def loadContent(self):
		self.player = Player("Max")
		self.player.loadImage('player.png')
		self.player.setPosition(100, 100)

if  __name__ =='__main__':
	game = Game()
	game.run()