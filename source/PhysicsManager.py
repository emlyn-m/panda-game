from abc import ABC, abstractmethod

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

    def collide(self, otherPhysicsManager):
        return Vector2()
