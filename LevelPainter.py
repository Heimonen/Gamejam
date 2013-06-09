import pygame, sys
from pygame.locals import *

from Entity import Entity

class LevelPainter:
    _levelfile = None

    def __init__(self, levelname, entities):
        self._levelfile = open(levelname, "r")
        self.drawLevel(entities)

    def drawLevel(self, entities):
        currentx, currenty = 0, 0
        try:
            for line in self._levelfile:
                for char in line:
                    if char != '\n':
                        self.addTile(char, entities, (currentx, currenty))
                        currentx = currentx + 32
                    else:
                        currentx = 0
                        currenty = currenty + 32
        finally:
            self._levelfile.close()
            pass
            
    def addTile(self, char, entities, xy):
        tile = Tile(char)
        tile.setPosition(xy[0], xy[1])
        entities.append(tile)

class Tile(Entity):
    _image = None

    def __init__(self, filename):
        Entity.__init__(self)
        self._image = pygame.image.load("tile"+filename+".png")
        
    def draw(self, surface):
        surface.blit(self._image, (self._x, self._y))
