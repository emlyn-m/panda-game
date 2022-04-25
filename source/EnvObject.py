import pygame
from Vector2 import Vector2
import math

class EnvironmentalObject:

    def __init__(self, graphicsManager, physicsManager):
        self.graphicsManager = graphicsManager
        self.physicsManager = physicsManager
