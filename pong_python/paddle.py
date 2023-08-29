import pygame
from game_object import GameObject


class Paddle(GameObject):
    def __init__(self, x_pos, y_pos, width, height, speed, color, field):
        super().__init__(x_pos, y_pos, color, field)
        self.width = width
        self.height = height
        self.speed = speed

        self.paddleRect = pygame.Rect(x_pos, y_pos, width, height)
        self.paddle = pygame.draw.rect(self.field, self.color, self.paddleRect)

    def update(self):
        self.paddle = pygame.draw.rect(self.field, self.color, self.paddleRect)

    def move(self):
        if (not (self.paddle.top + self.y_vel <= 0) and
                not (self.paddle.bottom + self.y_vel > self.field.get_size()[1])):
            self.y_pos += self.speed * self.y_vel

        self.paddleRect = (self.x_pos, self.y_pos, self.width, self.height)

    def get_rect(self):
        return self.paddle
