from Vector2 import Vector2

class PhysicsManager:

    GRAVITY = 9.81

    def __init__(self, mass, sizeXY, mu, posVec, hitbox):
        self.mass = mass
        self.areaX = sizeXY[0]
        self.areaY = sizeXY[1]
        self.mu = mu

        self.moveForce = 300000
        self.jumpForce = 700000

        self.pos = posVec
        self.velVec = Vector2()
        self.accel = Vector2()

        self.grounded = True
        self.hitbox = hitbox

        self.dT = 0


    def applyForce(self, forceVec):
        self.accel += forceVec * (1/self.mass)

    def tick(self, deltaT, objects):

        self.dT = deltaT

        self.velVec += self.accel * deltaT
        self.pos += self.velVec * deltaT

        # Handle collisions
        if self.velVec.getPolar()[0] != 0:  # Don't need to collide if not moving
            for obj in objects:
                obj.physicsManager.collide(self)

        self.velVec[0] *= (1-self.mu)
        self.accel[0] *= (1-self.mu)

        # Apply friction, gravity
        self.accel[1] += self.mass * PhysicsManager.GRAVITY * (not self.grounded)


    def collide(self, otherPhysicsManager):

        offset = (
            physicsManager.pos[0] - self.pos[0],
            physicsManager.pos[1] - self.pos[1]
        )

        dX = self.hitbox.overlap_area(physicsManager.hitbox, (offset[0] + 1, offset[1])) - self.hitbox.overlap_area(physicsManager.hitbox, (offset[0] - 1, offset[1]))
        dY = self.hitbox.overlap_area(physicsManager.hitbox, (offset[0], offset[1] + 1)) - self.hitbox.overlap_area(physicsManager.hitbox, (offset[0], offset[1] - 1))

        if dX != 0 or dY != 0:  # Collision
            collNormal = Vector2([dX, dY])

            print(collNormal.getNormalized())

            dV_r = (physicsManager.velVec * collNormal.getNormalized())
            dV_theta = collNormal.getPolar()[1]

            print(dV_theta)

            # sidetrack to check if grounded TODO

            dV = Vector2.fromPolar([-dV_r, dV_theta])

            print(dV, physicsManager.velVec)

            physicsManager.velVec += dV
            physicsManager.pos += dV * physicsManager.dT

            print(physicsManager.pos)
