import pygame
from Game.Colors import Colors
from Game.Player import Player
from Game.Image import Image
import random
import math


class Enemy():
    def __init__(self, window: pygame.Surface, window_width: int, window_height: int, img_path: str):
        # window
        self.window = window
        # window dimensions
        self.windowWidth = window_width
        self.windowHeight = window_height
        # image
        self.imgPath = img_path
        # colors
        self.colors = Colors()
        # enemy
        self.speed = 1.5
        self.minEnemies = 10
        self.enemies = []
        self.width = 21
        self.height = 31
        # keys
        self.keys = None
        self.rspeed = 2  # relative speed wrt gnd

    def draw(self, player: Player):
        # check which key(s) is pressed
        self.__getKeys()
        # move relatively
        self.__updatePoss()
        # create enemies at random positions
        self.__getEnemies()
        # follow the player
        self.__follow(player)

    def __follow(self, player: Player):
        for i in range(len(self.enemies)):
            enemyBB = self.enemies[i]['bb']
            enemyImage = self.enemies[i]['img']
            # calculate angle with player
            e_x = enemyBB.x
            e_y = enemyBB.y
            p_x = player.pos.x + player.pos.width / 2
            p_y = player.pos.y + player.pos.height / 2
            theta = math.atan(abs((e_y - p_y) / (e_x - p_x)))
            # calculate the direction(s)
            if e_x > p_x:
                x_direction = -1
            else:
                x_direction = 1
            if e_y > p_y:
                y_direction = -1
            else:
                y_direction = 1
            # update the position
            enemyBB.x += x_direction * self.speed * math.cos(theta)
            enemyBB.y += y_direction * self.speed * math.sin(theta)
            # show the enemy
            enemyImage.show(enemyBB)
            # self.__drawRect(enemyBB.x, enemyBB.y,
            #                 enemyBB.width, enemyBB.height,
            #                 self.colors.red, 1)

    def __getEnemies(self):
        if len(self.enemies) <= self.minEnemies:
            # calculate start position
            e_x = random.choice([random.randrange(-self.windowWidth, 0, self.width),
                                random.randrange(self.windowWidth, 2*self.windowWidth, self.width)])
            e_y = random.choice([random.randrange(-self.windowHeight, 0, self.height),
                                random.randrange(self.windowHeight, 2*self.windowHeight, self.height)])
            # enemy data
            enemy = {
                'bb': self.__getBB(e_x, e_y, self.width, self.height),
                'img': Image(self.window, self.imgPath, self.width, self.height)
            }
            self.enemies.append(enemy)

    def __getKeys(self):
        self.keys = pygame.key.get_pressed()

    def __updatePoss(self):
        if self.keys:
            # right arrow key
            if self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]:
                for enemy in self.enemies:
                    enemy['bb'].x -= self.rspeed
            # left arrow key
            elif self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]:
                for enemy in self.enemies:
                    enemy['bb'].x += self.rspeed
            # up arrow key
            if self.keys[pygame.K_UP] or self.keys[pygame.K_w]:
                for enemy in self.enemies:
                    enemy['bb'].y += self.rspeed
            # down arrow key
            elif self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]:
                for enemy in self.enemies:
                    enemy['bb'].y -= self.rspeed

    def __drawRect(self, x: int, y: int, width: int, height: int, color: tuple, _w: int):
        pygame.draw.rect(self.window,
                         color,
                         (x, y, width, height),
                         _w)

    def __getBB(self, x: int, y: int, w: int, h: int):
        return pygame.Rect(x, y, w, h)
