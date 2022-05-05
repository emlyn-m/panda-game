from Vector2 import Vector2
from GraphicsManager import GraphicsManager

class LevelScreen:
    def __init__(self, objs, size, bgPath, fpf, difficulty=0):
        self.__objs = objs
        self.pos = Vector2()
        self.size = Vector2(size)

        self.difficulty = difficulty

        self.graphicsManager = GraphicsManager(bgPath, fpf, size)


    def getObjs(self):
        return self.__objs

    def tick(self, dT, screen, pPos):

        survivingObjs = []

        self.graphicsManager.tick(screen, list(self.pos))

        if pPos[0] > self.size[0]*.25 and pPos[0] < self.size[0]*.75 and pPos[1] > self.size[1]*.25 and pPos[1] < self.size[1]*.75:
            # Reposition
            dPos = pPos - (self.size*.25)
            dPos[0] *= self.size[0]
            dPos[1] *= self.size[1]

            self.pos += dPos


        for obj in self.__objs:
            obj.tick(dT, screen, self.pos*-1)

            if not (abs(obj.physicsManager.pos[1]) > self.size[1]*1.25 and abs(obj.physicsManager.pos[0]) > self.size[0]*1.25):  # Kill all objs far beyond screen
                survivingObjs.append(obj)

        self.__objs = survivingObjs
