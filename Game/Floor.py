import pygame
from Game.Colors import Colors
from Game.Image import Image


class Floor():
    def __init__(self, window: pygame.Surface, window_width: int, window_height: int, img_width: int, img_height: int, img_path: str):
        # window
        self.window = window
        # window dimensions
        self.windowWidth = window_width
        self.windowHeight = window_height
        # colors
        self.colors = Colors()
        # IMAGE
        # path
        self.imgPath = img_path
        # dimensions
        self.imgWidth = img_width
        self.imgHeight = img_height
        # images
        self.floorImgs = self.__getImages()
        # positions
        self.imgPoss = self.__getPositions()

    def draw(self):
        for _img, _pos in zip(self.floorImgs, self.imgPoss):
            _img.show(_pos)

    def __getImages(self) -> list[Image]:
        imgs = []
        for i in range(8):
            img = Image(self.window, self.imgPath,
                        self.imgWidth, self.imgHeight)
            imgs.append(img)
        return imgs

    def __getPositions(self):
        return [self.__getBB(-self.windowWidth, -self.windowHeight,
                             self.windowWidth, self.windowHeight),
                self.__getBB(0, -self.windowHeight,
                             self.windowWidth, self.windowHeight),
                self.__getBB(self.windowWidth, -self.windowHeight,
                             self.windowWidth, self.windowHeight),
                self.__getBB(-self.windowWidth, 0,
                             self.windowWidth, self.windowHeight),
                self.__getBB(0, 0,
                             self.windowWidth, self.windowHeight),
                self.__getBB(self.windowWidth, 0,
                             self.windowWidth, self.windowHeight),
                self.__getBB(-self.windowWidth, self.windowHeight,
                             self.windowWidth, self.windowHeight),
                self.__getBB(0, self.windowHeight,
                             self.windowWidth, self.windowHeight),
                self.__getBB(self.windowWidth, self.windowHeight,
                             self.windowWidth, self.windowHeight)]

    def __drawRect(self, x: int, y: int, width: int, height: int, color: tuple, _w: int):
        pygame.draw.rect(self.window,
                         color,
                         (x, y, width, height),
                         _w)

    def __getBB(self, x: int, y: int, w: int, h: int):
        return pygame.Rect(x, y, w, h)
