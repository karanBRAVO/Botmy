import pygame
from Game.Colors import Colors


class Player():
    def __init__(self, window: pygame.Surface, window_width: int, window_height: int):
        # window
        self.window = window
        # window dimensions
        self.windowWidth = window_width
        self.windowHeight = window_height
        # position and dimensions
        self.pos = self.__getBB(self.windowWidth // 2,
                                self.windowHeight // 2,
                                15, 15)
        # colors
        self.colors = Colors()
        # keys
        self.keys = None
        # speed
        self.speed = 2

    def draw(self):
        # check which key(s) is pressed
        self.__getKeys()
        # update the position of the player
        self.__updatePos()
        # (re)draw at the updated position
        self.__drawRect(self.pos.x, self.pos.y,
                        self.pos.width, self.pos.height,
                        self.colors.blue, 0)

    def __updatePos(self):
        if self.keys:
            # right arrow key
            if self.keys[pygame.K_RIGHT] and self.pos.x < self.windowWidth - (2 * self.pos.width):
                self.pos.x += self.speed
            # left arrow key
            elif self.keys[pygame.K_LEFT] and self.pos.x > self.pos.width:
                self.pos.x -= self.speed
            # up arrow key
            if self.keys[pygame.K_UP] and self.pos.y > self.pos.height:
                self.pos.y -= self.speed
            # down arrow key
            elif self.keys[pygame.K_DOWN] and self.pos.y < self.windowHeight - (2 * self.pos.height):
                self.pos.y += self.speed

    def __getKeys(self):
        self.keys = pygame.key.get_pressed()

    def __drawRect(self, x: int, y: int, w: int, h: int, color: tuple, _w: int):
        pygame.draw.rect(self.window,
                         color,
                         (x, y, w, h), _w)

    def __getBB(self, x: int, y: int, w: int, h: int):
        return pygame.Rect(x, y, w, h)
