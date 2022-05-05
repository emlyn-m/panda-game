import os
import pygame

from Queue import Queue

class Animation:

    def __init__(self, fPath, fpf, size):
        self.size = size
        self.__fIdx = 0
        self.__fpf = fpf

        self.__lastFrame = None
        self.frames = self.__loadAnim(fPath)
        self.allFrames = self.frames  # Used for resetting without reloading

        self.killable = False

    def reset(self):
        self.__fIdx = 0
        self.killable = False
        self.frames = allFrames

    def tick(self, dFrames):
        self.__fIdx += dFrames
        if self.__fIdx >= self.__fpf:
            self.__fIdx = 0
            self.__lastFrame = self.frames.dequeue()
            return self.__lastFrame
        else:
            return self.__lastFrame

        if len(self.frames) == 0:
            self.killable = True

    def __loadAnim(self, fPath):
        if not os.path.exists(fPath):  # Check path exists
            return None

        if len(os.listdir(fPath)) == 0:  # Check frames exist
            return None

        frames = []
        for fName in os.listdir(fPath):
            frames.append(pygame.image.load(fPath + fName).convert_alpha())
            frames[-1] = pygame.transform.scale(frames[-1], self.size)

        animQueue = Queue(len(frames))
        for frame in frames:
            animQueue.enqueue(frame)

        return animQueue
