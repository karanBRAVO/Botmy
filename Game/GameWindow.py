import pygame
from pygame.locals import *
import sys
from Game.Colors import Colors
from Game.Floor import Floor
from Game.Player import Player
from Game.Particles import Particles
from Game.Score import Score
from Game.Bullet import Bullet
from Game.Enemy import Enemy


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
        pygame.display.set_caption("Botmy")
        # clock
        self.clock = pygame.time.Clock()
        self.fps = 60
        # states
        self.run = True
        # Floor
        self.floor = Floor(self.window,
                           self.windowWidth, self.windowHeight,
                           self.windowWidth, self.windowHeight,
                           "assets/floor.jpg")
        # player
        self.player = Player(self.window,
                             self.windowWidth, self.windowHeight,
                             "assets/player.png")
        # particles
        self.particles = Particles(self.window,
                                   self.windowWidth, self.windowHeight,
                                   "assets/particle.png")
        # score
        self.score = Score(self.window,
                           self.windowWidth, self.windowHeight)
        # bullets
        self.bullet = Bullet(self.window,
                             self.windowWidth, self.windowHeight,
                             "assets/bullet.png")
        # enemy
        self.enemy = Enemy(self.window,
                           self.windowWidth, self.windowHeight,
                           "assets/enemy.png")

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
        self.particles.draw()
        self.score.draw(self.player.pos, self.particles.particles)
        self.bullet.draw(self.player, self.enemy)
        self.player.draw()
        self.enemy.draw(self.player)

    def __update(self):
        pygame.display.update()
        self.clock.tick(self.fps)

    def __quit(self):
        pygame.quit()
        sys.exit(0)
