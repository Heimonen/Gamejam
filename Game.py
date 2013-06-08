import pygame, sys
from pygame.locals import *

class Game:
	windowSurface = None
	fpsClock = pygame.time.Clock()

	def run(self):
		self.init()
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
		# draw a green polygon onto the surface
		pygame.draw.polygon(self.windowSurface, (0,255,0), ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
		# draw the window onto the screen
		pygame.display.update()

	def init(self):
		pygame.init()
		# set up the window
		self.windowSurface = pygame.display.set_mode((1024, 768), 0, 32)

if  __name__ =='__main__':
	game = Game()
	game.run()