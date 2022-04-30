import pygame
import os

class GraphicsManager:
    def __init__(self, spritePath, lengthMultiplier, sizeXY):
        self.sizeXY = sizeXY
        self.spriteFrames = self.loadAnim(spritePath, lengthMultiplier)

        self.idleLengthMultiplier = lengthMultiplier
        self.idleFrames = self.spriteFrames

    def loadAnim(self, animFramesPath, lengthMultiplier):

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
        screen.blit(self.spriteFrames[int(self.activeFrameIdx)], pos)
        self.activeFrameIdx += 1/self.lengthMultiplier  # TODO: Find some better way to do this avoiding floating point rounding errors
        # ACTUALLY dont fix this JUST yet, it'll be a cool point for second presentation (easily fixable with round(n, 7))

        if self.activeFrameIdx >= len(self.spriteFrames):
            self.spriteFrames = self.idleFrames  # Each anim should only play once
            self.lengthMultiplier = self.idleLengthMultiplier
            self.activeFrameIdx = 0
