import pygame
import math

from GraphicsManager import GraphicsManager
from CollidablePhysicsManager import CollidablePhysicsManager

class EnvironmentalObject:

    def __init__(self, framesPath, fpf, size, posVec):
        self.graphicsManager = GraphicsManager(framesPath, fpf, size)
        self.physicsManager = CollidablePhysicsManager(999, size, 0, posVec, pygame.mask.Mask(size, fill=True))

    def tick(self, dT, screen):
        self.physicsManager.tick(dT)
        self.graphicsManager.tick(screen, list(self.physicsManager.pos))
