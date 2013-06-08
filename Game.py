class Game:

	def run(self):
		# Game Loop
		while(True):
			update()
			draw()

	def update(self):
		pass

	def draw(self):
		pass

if  __name__ =='__main__':
	game = Game()
	game.run()