import pygame
from Game.Colors import Colors


class Floor():
    def __init__(self, window: pygame.Surface, width: int, height: int, path: str):
        # window
        self.window = window
        # assets path
        self.path = path
        # colors
        self.colors = Colors()
        # dimensions
        self.width = width
        self.height = height
        # image
        self.image = None
        # positions
        self.pos = [self.__getBB(-self.width, -self.height,
                                 self.width, self.height),
                    self.__getBB(0, -self.height,
                                 self.width, self.height),
                    self.__getBB(self.width, -self.height,
                                 self.width, self.height),
                    self.__getBB(-self.width, 0,
                                 self.width, self.height),
                    self.__getBB(0, 0,
                                 self.width, self.height),
                    self.__getBB(self.width, 0,
                                 self.width, self.height),
                    self.__getBB(-self.width, self.height,
                                 self.width, self.height),
                    self.__getBB(0, self.height,
                                 self.width, self.height),
                    self.__getBB(self.width, self.height,
                                 self.width, self.height)]
        # load the image
        self.__loadImage()

    def draw(self):
        for _p in self.pos:
            self.__showImage(_p)

    def __showImage(self, pos: pygame.Rect):
        if self.image:
            self.window.blit(self.image, pos)

    def __loadImage(self):
        try:
            self.image = pygame.transform.scale(pygame.image.load(self.path),
                                                (self.width, self.height))
        except Exception as e:
            print(e)

    def __drawRect(self, x: int, y: int, width: int, height: int, color: tuple, _w: int):
        pygame.draw.rect(self.window,
                         color,
                         (x, y, width, height),
                         _w)

    def __getBB(self, x: int, y: int, w: int, h: int):
        return pygame.Rect(x, y, w, h)
