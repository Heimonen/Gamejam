import pygame, sys, pygame.mixer
from pygame.locals import *


class SoundHandler:

	def __init__(self):
		pygame.mixer.pre_init()
		pygame.mixer.init()

	@staticmethod
	def playSound(soundName):
		soundEffect = pygame.mixer.Sound(soundName)
		soundEffect.play()

	@staticmethod
	def playSong(songName):
		pygame.mixer.music.load(songName)
		pygame.mixer.music.set_volume(.9)
		pygame.mixer.music.play(-1)