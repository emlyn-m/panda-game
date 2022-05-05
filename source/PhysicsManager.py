from abc import ABC, abstractmethod
from Vector2 import Vector2

class PhysicsManager(ABC):

    def __init__(self, mass, sizeXY, mu, posVec, hitboxMask):
        self.mass = mass
        self.areaX = sizeXY[0]
        self.areaY = sizeXY[1]
        self.mu = mu

        self.pos = posVec
        self.hitbox = hitboxMask

        self.grounded = True

        self.dT = 0

    @abstractmethod
    def tick(self, dT, objs):
        pass


    def checkCollision(self, deltaT, objs):
        self.dT = deltaT

        # Handle collisions
        collNormals = []
        for obj in objs:
            collNormals.append(obj.physicsManager.collide(self))

        groundedCN = Vector2([0, 1])
        for cn in collNormals:
            if list(cn) == list(groundedCN):

                if not self.grounded: self.accel[1] = 0  # Only reset fall accel on first ground collision otherwise cannot jump

                self.grounded = True
                break
        else:
            self.grounded = False



    def collide(self, otherPhysicsManager):
        return Vector2()
