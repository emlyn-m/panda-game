from EnvObject import EnvironmentalObject
from CollidablePhysicsManager import CollidablePhysicsManager

class HazardPhysicsManager(CollidablePhysicsManager):

    def collide(self, otherPhysicsManager):
        cv = super().collide(otherPhysicsManager)
        if list(cv) != [0, 0]:
            # Move to dead zone


class Hazard(EnvironmentalObject):
    def __init__(self, framesPath, fpf, size, posVec):
        super().__init__(framesPath, fpf, size, posV)
        self.physicsManager = HazardPhysicsManager(mass, sizeXY, mu, posVec, pygame.mask.Mask(size, fill=True))
