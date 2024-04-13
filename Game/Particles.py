import pygame
from Game.Colors import Colors
from Game.Image import Image
import random


class Particles():
    def __init__(self, window: pygame.Surface, window_width: int, window_height: int, img_path: str):
        # window
        self.window = window
        # window dimensions
        self.windowWidth = window_width
        self.windowHeight = window_height
        # colors
        self.colors = Colors()
        # image
        self.imgPath = img_path
        self.images: list[Image] = []
        # particles
        self.width = 20
        self.height = 20
        self.particles: list[pygame.Rect] = []
        # minimum particles on the floor at given time
        self.minParticles = 10
        # maximum particles on the floor at given time
        self.maxParticles = 100
        # keys
        self.keys = None
        # speed
        self.speed = 2

    def draw(self):
        # generate new particles
        self.__generateRandomParticles()
        # check which key(s) is pressed
        self.__getKeys()
        # update the position
        self.__updatePoss()
        # correct the position
        self.__correctPosition()
        # draw the particle on the screen
        self.__showParticles()

    def __correctPosition(self):
        for _pos in self.particles:
            if _pos.x <= -2 * self.windowWidth:
                _pos.x = self.windowWidth
            if _pos.x >= 2 * self.windowWidth:
                _pos.x = -self.windowWidth
            if _pos.y >= 2 * self.windowHeight:
                _pos.y = -self.windowHeight
            if _pos.y <= -2 * self.windowHeight:
                _pos.y = self.windowHeight

    def __updatePoss(self):
        if self.keys:
            # right arrow key
            if self.keys[pygame.K_RIGHT]:
                for _pos in self.particles:
                    _pos.x -= self.speed
            # left arrow key
            elif self.keys[pygame.K_LEFT]:
                for _pos in self.particles:
                    _pos.x += self.speed
            # up arrow key
            if self.keys[pygame.K_UP]:
                for _pos in self.particles:
                    _pos.y += self.speed
            # down arrow key
            elif self.keys[pygame.K_DOWN]:
                for _pos in self.particles:
                    _pos.y -= self.speed

    def __getKeys(self):
        self.keys = pygame.key.get_pressed()

    def __showParticles(self):
        for _img, particle in zip(self.images, self.particles):
            _img.show(particle)
            # self.__drawRect(particle.x, particle.y,
            #                 particle.width, particle.height,
            #                 self.colors.pink, 0)

    def __generateRandomParticles(self):
        if len(self.particles) <= self.minParticles:
            for i in range(self.maxParticles):
                x = random.randint(-self.windowWidth, self.windowHeight)
                y = random.randint(-self.windowHeight, self.windowHeight)
                particle = self.__getBB(x, y,
                                        self.width, self.height)
                self.particles.append(particle)
                img = Image(self.window, self.imgPath,
                            self.width, self.height)
                self.images.append(img)

    def __drawRect(self, x: int, y: int, width: int, height: int, color: int, _w: int):
        pygame.draw.rect(self.window,
                         color,
                         (x, y, width, height),
                         _w)

    def __getBB(self, x: int, y: int, w: int, h: int):
        return pygame.Rect(x, y, w, h)
