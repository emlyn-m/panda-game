import pygame
import time
import platform

from GraphicsManager import GraphicsManager
from MovablePhysicsManager import MovablePhysicsManager
from Vector2 import Vector2
from ScoreRecord import Scores, ScoreRecord

class Player():

    def __init__(self, framesPath, fpf, size, mass, mu, posVec):
        self.graphicsManager = GraphicsManager(framesPath, fpf, size)
        self.physicsManager = MovablePhysicsManager(mass, size, mu, posVec, pygame.mask.Mask(size, fill=True))

        self.beginUnixTime = time.time()
        self.rtaMs = 0

        self.moveForce = 300000  # Default values
        self.jumpForce = 850000

    def tick(self, dT, objs, screen):
        self.physicsManager.tick(dT, objs)
        self.graphicsManager.tick(screen, list(self.physicsManager.pos))

        self.rtaMs += dT


    def walk(self, dirVector):
        self.physicsManager.applyForce(dirVector * self.moveForce)

    def jump(self):
        if self.physicsManager.grounded:
            jumpCoefficient = self.jumpForce + (self.physicsManager.velVec.getPolar()[0] * 1000)
            self.physicsManager.applyForce(Vector2([0,-1]) * jumpCoefficient)


    def exportTime(self, outputPath):
        existingScores = Scores(outputPath)
        newScore = {"name": platform.node, "startTime": self.beginUnixTime, "rtaMs": self.rtaMs}
        existingScores.add(newScore)
        existingScores.write(outputPath)
