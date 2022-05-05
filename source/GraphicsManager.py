import pygame
import os

from Stack import Stack
from Animation import Animation

class GraphicsManager:
    def __init__(self, spritePath, lengthMultiplier, sizeXY):
        self.sizeXY = sizeXY
        self.animStack = Stack(5)  # Unlikely to need more than 5 animations at once

        self.activeAnim = Animation(spritePath, lengthMultiplier, sizeXY)
        self.animStack.push(self.activeAnim)

    def __loadAnim(self, animFramesPath, lengthMultiplier):

        self.activeFrameIdx = 0  # Reset animation
        self.lengthMultiplier = lengthMultiplier

        if not os.path.exists(animFramesPath):  # Check path exists
            return None

        if len(os.listdir(animFramesPath)) == 0:  # Check frames exist
            return None

        frames = []
        for fName in os.listdir(animFramesPath):
            frames.append(pygame.image.load(animFramesPath + fName).convert_alpha())
            frames[-1] = pygame.transform.scale(frames[-1], self.sizeXY)

        return frames


    def tick(self, screen, pos):

        if (self.activeAnim.killable):
            newActiveAnim = self.animStack.pop()
            if newActiveAnim:  # Return None if no animation next
                self.activeAnim = newActiveAnim
            else:
                self.activeAnim.reset()

        newFrame = self.activeAnim.frames.dequeue()
        screen.blit(newFrame, pos)

        self.activeAnim.tick(1)
