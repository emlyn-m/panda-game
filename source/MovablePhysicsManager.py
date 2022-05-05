from Vector2 import Vector2
from PhysicsManager import PhysicsManager
import constants

class MovablePhysicsManager(PhysicsManager):

    def __init__(self, mass, sizeXY, mu, posVec, hbMask):
        super().__init__(mass, sizeXY, mu, posVec, hbMask)

        self.velVec = Vector2()
        self.accel = Vector2()

        self.applyForce(Vector2())  # No clue why needed but oh well


    def applyForce(self, forceVec):
        self.accel += forceVec * (1/self.mass)

    def __move(self, dT):
        if not self.grounded: self.accel[1] += self.mass * constants.GRAVITY


        self.velVec += self.accel * dT
        self.pos += self.velVec * dT

        self.accel[0] *= self.mu
        self.velVec[0] *= self.mu

    def tick(self, deltaT, objects):

        self.__move(deltaT)

        self.checkCollision(deltaT, objects)

        self.accel *= self.mu
