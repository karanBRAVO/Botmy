import pygame
from Game.Colors import Colors
from Game.Image import Image


class Player():
    def __init__(self, window: pygame.Surface, window_width: int, window_height: int, img_path: str):
        # window
        self.window = window
        # window dimensions
        self.windowWidth = window_width
        self.windowHeight = window_height
        # position and dimensions
        self.pos = self.__getBB(self.windowWidth // 2,
                                self.windowHeight // 2,
                                35, 41)
        # colors
        self.colors = Colors()
        # image
        self.imgPath = img_path
        self.image = Image(self.window, self.imgPath,
                           self.pos.width, self.pos.height)
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
        self.__show()

    def __show(self):
        self.image.show(self.pos)
        # self.__drawRect(self.pos.x, self.pos.y,
        #                 self.pos.width, self.pos.height,
        #                 self.colors.blue, 2)

    def __updatePos(self):
        if self.keys:
            # right arrow key
            if (self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]) and self.pos.x < self.windowWidth - (2 * self.pos.width):
                self.pos.x += self.speed
            # left arrow key
            elif (self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]) and self.pos.x > self.pos.width:
                self.pos.x -= self.speed
            # up arrow key
            if (self.keys[pygame.K_UP] or self.keys[pygame.K_w]) and self.pos.y > self.pos.height:
                self.pos.y -= self.speed
            # down arrow key
            elif (self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]) and self.pos.y < self.windowHeight - (2 * self.pos.height):
                self.pos.y += self.speed

    def __getKeys(self):
        self.keys = pygame.key.get_pressed()

    def __drawRect(self, x: int, y: int, w: int, h: int, color: tuple, _w: int):
        pygame.draw.rect(self.window,
                         color,
                         (x, y, w, h), _w)

    def __getBB(self, x: int, y: int, w: int, h: int):
        return pygame.Rect(x, y, w, h)
