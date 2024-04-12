import pygame


class Image():
    def __init__(self, window: pygame.Surface, path: str, width: int, height: int):
        # window
        self.window = window
        # path
        self.path = path
        # dimensions
        self.width = width
        self.height = height
        # image
        self.image = None
        self.__load()

    def show(self, pos: pygame.Rect):
        if self.image:
            self.window.blit(self.image, pos)

    def __load(self):
        try:
            self.image = pygame.transform.scale(pygame.image.load(self.path),
                                                (self.width, self.height))
        except Exception as e:
            print(e)
