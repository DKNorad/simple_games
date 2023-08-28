import pygame
from game_object import GameObject
from random import choice


class Ball(GameObject):
    def __init__(self, x_pos, y_pos, radius, speed, color, field):
        super().__init__(x_pos, y_pos, color, field)
        self.center = (x_pos, y_pos)
        self.radius = radius
        self.speed = speed

        self.is_initial = True
        self.ball = pygame.draw.circle(self.field, self.color, (self.x_pos, self.y_pos), self.radius)

    def update(self):
        self.ball = pygame.draw.circle(self.field, self.color, (self.x_pos, self.y_pos), self.radius)

    def move(self):
        if self.is_initial:
            self.y_vel = choice([-1, 1])
            self.x_vel = choice([-1, 1])
            self.is_initial = False

        if self.y_pos - self.radius <= 0:
            self.y_vel *= -1
        elif self.y_pos + self.radius >= self.field.get_size()[1]:
            self.y_vel *= -1

        self.y_pos += self.speed * self.y_vel
        self.x_pos += self.speed * self.x_vel

    def hit(self):
        self.x_vel *= -1

    def reset(self):
        self.is_initial = True
        self.x_pos = self.center[0]
        self.y_pos = self.center[1]

    def get_rect(self):
        return self.ball

