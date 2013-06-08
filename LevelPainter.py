import pygame, sys
from pygame.locals import *

from Entity import Entity

class LevelPainter:
    _levelfile = None

    def __init__(self, levelname, entities):
        self._levelfile = open(levelname, "r")
        self.drawLevel(entities)

    def drawLevel(self, entities):
        try:
            for line in self._levelfile:
                for char in line:
                    self.addTile(char, entities)
        finally:
            self._levelfile.close()
            pass
            
    def addTile(self, char, entities):
        tile = Tile(char)
        entities.append(tile)

class Tile(Entity):
    _image = None

    def __init__(self, filename):
        Entity.__init__(self)
        # print "tile"+filename+".png"
        self._image = pygame.image.load("tile"+filename+".png")
        
    def draw(self, surface):
        surface.blit(self._image, (self._x, self._y))
