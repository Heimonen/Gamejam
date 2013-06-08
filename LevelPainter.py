import pygame, sys
from pygame.locals import *

class LevelPainter:

    def __init__(self, levelname):
        levelfile = open(levelname)
        try:
            for line in levelfile:
                for char in line:
                    pass
        finally:
            levelfile.close()
