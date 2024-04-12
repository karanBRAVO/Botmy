import pygame
from pygame.locals import *
import sys
from Game.Colors import Colors
from Game.Floor import Floor


class Game():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        # initialize colors
        self.colors = Colors()
        # window dimensions
        self.windowWidth = 500
        self.windowHeight = 400
        # window
        self.window = pygame.display.set_mode((self.windowWidth,
                                              self.windowHeight))
        pygame.display.set_caption("Game Development")
        # clock
        self.clock = pygame.time.Clock()
        self.fps = 60
        # states
        self.run = True
        # Floor
        self.floor = Floor(self.window,
                           self.windowWidth, self.windowHeight,
                           "assets/floor.jpg")

    def start(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.run = False
            self.__draw()
            self.__update()
        self.__quit()

    def __draw(self):
        self.window.fill(self.colors.white)
        self.floor.draw()

    def __update(self):
        pygame.display.update()
        self.clock.tick(self.fps)

    def __quit(self):
        pygame.quit()
        sys.exit(0)
