from PhysicsManager import PhysicsManager
from Vector2 import Vector2
import constants

class CollidablePhysicsManager(PhysicsManager):

    def tick(self, dT):
        pass  # Must be declared as abstract

    def collide(self, physicsManager):

        offset = (
            physicsManager.pos[0] - self.pos[0],
            physicsManager.pos[1] - self.pos[1]
        )

        dX = self.hitbox.overlap_area(physicsManager.hitbox, (offset[0] + 1, offset[1])) - self.hitbox.overlap_area(physicsManager.hitbox, (offset[0] - 1, offset[1]))
        dY = self.hitbox.overlap_area(physicsManager.hitbox, (offset[0], offset[1] + 1)) - self.hitbox.overlap_area(physicsManager.hitbox, (offset[0], offset[1] - 1))

        if dX != 0 or dY != 0:  # Collision
            collVec = Vector2([dX, dY]).getNormalized()
            dV_r = collVec * physicsManager.velVec  # TODO: Fix this to fix stall far away bug
            dV = collVec * dV_r

            if collVec.getPolar()[1] >= 0:  # For some reason dV_r has theta ALWAYS > 0
                dV *= -1

            physicsManager.velVec += dV
            physicsManager.pos += dV * physicsManager.dT

            return collVec

        return Vector2()
