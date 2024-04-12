import pygame
from Game.Colors import Colors


class Score():
    def __init__(self, window: pygame.Surface, window_width: int, window_height: int):
        # window
        self.window = window
        # window dimensions
        self.windowWidth = window_width
        self.windowHeight = window_height
        # score
        self.score = 0
        # font
        self.font = pygame.font.SysFont('monospace', 11, True, False)
        # colors
        self.colors = Colors()
        # score position
        self.scorePos = (0, 0)

    def draw(self, player: pygame.Rect, particles: list[pygame.Rect]):
        # detect the player and particles collision
        self.__detectCollision(player, particles)
        # show the score
        self.__show()

    def __show(self):
        score = self.font.render(f"score: {self.score}", True, self.colors.red)
        self.window.blit(score, self.scorePos)

    def __update(self):
        self.score += 1

    def __detectCollision(self, player: pygame.Rect, particles: list[pygame.Rect]):
        for i in range(len(particles)):
            particle = particles[i]
            if particle.colliderect(player):
                self.__update()
                particles.pop(i)
                break
