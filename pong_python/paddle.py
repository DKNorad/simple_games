import pygame


class Paddle(pygame.sprite.Sprite):
    SPEED = 10

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)


    def move(self, y):
        pass
