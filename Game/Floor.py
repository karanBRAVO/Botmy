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
        # keys
        self.keys = None
        # speed
        self.speed = 2

    def draw(self):
        # check which key(s) is pressed
        self.__getKeys()
        # update the position
        self.__updatePoss()
        # correct the position
        self.__correctPosition()
        # draw at the updated position
        for _img, _pos in zip(self.floorImgs, self.imgPoss):
            _img.show(_pos)
            # self.__drawRect(_pos.x, _pos.y,
            #                 _pos.width, _pos.height,
            #                 self.colors.red, 10)

    def __correctPosition(self):
        for _pos in self.imgPoss:
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
            if self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]:
                for _pos in self.imgPoss:
                    _pos.x -= self.speed
            # left arrow key
            elif self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]:
                for _pos in self.imgPoss:
                    _pos.x += self.speed
            # up arrow key
            if self.keys[pygame.K_UP] or self.keys[pygame.K_w]:
                for _pos in self.imgPoss:
                    _pos.y += self.speed
            # down arrow key
            elif self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]:
                for _pos in self.imgPoss:
                    _pos.y -= self.speed

    def __getKeys(self):
        self.keys = pygame.key.get_pressed()

    def __getImages(self) -> list[Image]:
        imgs = []
        for i in range(9):
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
