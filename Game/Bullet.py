import pygame
import math
from Game.Colors import Colors
from Game.Image import Image
from Game.Player import Player


class Bullet():
    def __init__(self, window: pygame.Surface, window_width: int, window_height: int, img_path: str):
        # window
        self.window = window
        self.windowWidth = window_width
        self.windowHeight = window_height
        # colors
        self.colors = Colors()
        # image
        self.imgPath = img_path
        # bullets
        self.speed = .19
        self.minBulletCount = 10
        self.bullets: list[dict] = []

    def draw(self, player: Player):
        # calculate bullet metrics [direction, angle, startPoint]
        self.__checkFire(player)
        # fire the bullet
        self.__fire()

    def __fire(self):
        for i in range(len(self.bullets)):
            bullet = self.bullets[i]
            # update the bullet position
            bullet['bb'].x += (self.speed * bullet['direction']
                               [0]) * math.degrees(math.cos(bullet['angle']))
            bullet['bb'].y += (self.speed * bullet['direction']
                               [1]) * math.degrees(math.sin(bullet['angle']))
            # show the bullet
            bullet['img'].show(bullet['bb'])
            # self.__drawRect(bullet['bb'].x, bullet['bb'].y,
            #                 bullet['bb'].width, bullet['bb'].height,
            #                 self.colors.red, 0)
            # remove the bullet outside window
            if bullet['bb'].x < 0 or bullet['bb'].y < 0 or bullet['bb'].x > self.windowWidth or bullet['bb'].y > self.windowHeight:
                self.bullets.pop(i)
                break

    def __checkFire(self, player: Player):
        if len(self.bullets) <= self.minBulletCount:
            if pygame.mouse.get_pressed(3)[0]:
                # mouse position
                m_x, m_y = pygame.mouse.get_pos()
                # player position
                p_x = player.pos.x + player.pos.width / 2
                p_y = player.pos.y + player.pos.height / 2
                # calculating the direction and angle
                if m_x > p_x:
                    x_direction = 1
                else:
                    x_direction = -1
                if m_y > p_y:
                    y_direction = 1
                else:
                    y_direction = -1
                theta = math.atan(abs((p_y-m_y)/(p_x-m_x)))
                # bullet data
                _bullet_ = {
                    'bb': self.__getBB(p_x, p_y, 5, 5),
                    'img': Image(self.window, self.imgPath, 10, 10),
                    'direction': [x_direction, y_direction],
                    'angle': theta,
                }
                self.bullets.append(_bullet_)

    def __drawRect(self, x: int, y: int, width: int, height: int, color: tuple, _w: int):
        pygame.draw.rect(self.window,
                         color,
                         (x, y, width, height),
                         _w)

    def __getBB(self, x: int, y: int, w: int, h: int):
        return pygame.Rect(x, y, w, h)
