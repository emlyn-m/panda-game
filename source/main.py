#!/usr/bin/env python3
"""Main program."""

import random
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Hide annoying message
import pygame

from Vector2 import Vector2
from Player import Player
from GraphicsManager import GraphicsManager
from PhysicsManager import PhysicsManager
from EnvObject import EnvironmentalObject


def safeQuit():
    """Quit safely."""
    pygame.quit()
    quit()


def __main__():

    fps = 60
    fpsClock = pygame.time.Clock()

    pygame.init()
    screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

    # Initialize player
    playerGraphicsManager = GraphicsManager("../assets/panda.idle/", 3.5, (100, 100))
    playerPhysicsManager = PhysicsManager(100, (100, 175), .3, Vector2([0, 680]), pygame.mask.from_surface(playerGraphicsManager.idleFrames[0]))
    mPlayer = Player(playerGraphicsManager, playerPhysicsManager)

    testObjGraphicsManager = GraphicsManager("../assets/panda.idle/", 1, (50, 50))
    testObjPhysicsManager = PhysicsManager(0, (50, 50), 1, Vector2([200, 200]), pygame.mask.from_surface(testObjGraphicsManager.idleFrames[0]))
    testObj = EnvironmentalObject(testObjGraphicsManager, testObjPhysicsManager)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                safeQuit()

        # Handle inputs
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_LEFT]:
            mPlayer.physicsManager.applyForce(Vector2([-1, 0]) * mPlayer.physicsManager.moveForce)

        if pressedKeys[pygame.K_RIGHT]:
            mPlayer.physicsManager.applyForce(Vector2([1, 0]) * mPlayer.physicsManager.moveForce)

        if pressedKeys[pygame.K_UP] or pressedKeys[pygame.K_c]:
            if mPlayer.physicsManager.grounded:
                mPlayer.physicsManager.applyForce(Vector2([0, -1]) * mPlayer.physicsManager.jumpForce)
                mPlayer.physicsManager.grounded = False

        if pressedKeys[pygame.K_x]:
            pass  # Special action

        mPlayer.physicsManager.tick(1/fps, [testObj])  # TODO: Replace [] with env objs

        screen.fill((0, 0, 0))
        mPlayer.graphicsManager.draw(screen, mPlayer.physicsManager.pos.getValues())

        for obj in [testObj]:
            obj.graphicsManager.draw(screen, obj.physicsManager.pos.getValues())

        # TODO: Draw all environmental objects

        pygame.display.flip()
        fpsClock.tick(fps)  # Cap at 60 FPS


if __name__ == '__main__':
    __main__()
