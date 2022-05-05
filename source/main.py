#!/usr/bin/env python3
"""Main program."""

import random
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # Hide annoying message
import pygame

from Vector2 import Vector2
from Player import Player
from GraphicsManager import GraphicsManager
from MovablePhysicsManager import MovablePhysicsManager
from CollidablePhysicsManager import CollidablePhysicsManager
from EnvObject import EnvironmentalObject
from LevelScreen import LevelScreen


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
    mPlayer = Player("../assets/panda/idle/", 3.5, (100, 100), 100, .7, Vector2([250, 0]))
    testObj = EnvironmentalObject("../assets/panda/idle/", 1, (200, 200), Vector2([250, 580]))

    mLevelScreen = LevelScreen([testObj], (1920, 1080), "../assets/background/screen1/", 10)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                safeQuit()

        # Handle inputs
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_LEFT]:
            mPlayer.walk(Vector2([-1, 0]))

        if pressedKeys[pygame.K_RIGHT]:
            mPlayer.walk(Vector2([1, 0]))

        if pressedKeys[pygame.K_UP] or pressedKeys[pygame.K_c]:
            mPlayer.jump()

        if pressedKeys[pygame.K_x]:
            pass  # Special action

        screen.fill((0, 0, 0))

        mLevelScreen.tick(1/fps, screen, mPlayer.physicsManager.pos)
        mPlayer.tick(1/fps, mLevelScreen.getObjs() , screen)

        pygame.display.flip()
        fpsClock.tick(fps)  # Cap at 60 FPS


if __name__ == '__main__':
    __main__()
