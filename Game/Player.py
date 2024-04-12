import pygame
from Game.Colors import Colors


class Player():
    def __init__(self, window: pygame.Surface, x: int, y: int):
        # window
        self.window = window
        # position and dimensions
        self.pos = self.__getBB(x, y, 15, 15)
        # colors
        self.colors = Colors()

    def draw(self):
        self.__drawRect(self.pos.x, self.pos.y,
                        self.pos.width, self.pos.height,
                        self.colors.blue, 0)

    def __drawRect(self, x: int, y: int, w: int, h: int, color: tuple, _w: int):
        pygame.draw.rect(self.window,
                         color,
                         (x, y, w, h), _w)

    def __getBB(self, x: int, y: int, w: int, h: int):
        return pygame.Rect(x, y, w, h)
