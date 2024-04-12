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
        self.speed = 1

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
            if self.keys[pygame.K_RIGHT]:  # right arrow key
                self.pos.x += self.speed
            elif self.keys[pygame.K_LEFT]:  # left arrow key
                self.pos.x -= self.speed
            elif self.keys[pygame.K_UP]:  # up arrow key
                self.pos.y -= self.speed
            elif self.keys[pygame.K_DOWN]:  # down arrow key
                self.pos.y += self.speed

    def __getKeys(self):
        self.keys = pygame.key.get_pressed()

    def __drawRect(self, x: int, y: int, w: int, h: int, color: tuple, _w: int):
        pygame.draw.rect(self.window,
                         color,
                         (x, y, w, h), _w)

    def __getBB(self, x: int, y: int, w: int, h: int):
        return pygame.Rect(x, y, w, h)
