import pygame
from game_object import GameObject
from random import randint


class Ball(GameObject):
    MAX_Y_VEL = 5

    def __init__(self, x_pos, y_pos, radius, color, field):
        super().__init__(x_pos, y_pos, color, field)
        self.center = (x_pos, y_pos)
        self.width = x_pos * 2
        self.height = y_pos * 2
        self.radius = radius
        self.hits = 0
        self.x_vel = 10

        self.is_initial = True
        self.ball = pygame.draw.circle(self.field, self.color, (self.x_pos, self.y_pos), self.radius)

    def update(self):
        self.ball = pygame.draw.circle(self.field, self.color, (self.x_pos, self.y_pos), self.radius)

    def handle_movement(self):
        if self.is_initial:
            self.x_vel = 7
            self.y_vel = randint(-5, 5)
            self.is_initial = False
        else:
            self.x_vel = self.x_vel
        self.y_pos += self.y_vel
        self.x_pos += self.x_vel

    def hit(self, y_vel):
        self.hits += 1
        self.x_vel *= -1
        self.y_vel = -1 * y_vel

        # Increase the speed every 5 hits.
        if self.hits % 5 == 0:
            self.x_vel *= 1.05

    def reset(self):
        self.is_initial = True
        self.x_pos = self.center[0]
        self.y_pos = self.center[1]
        self.hits = 0

    def get_rect(self):
        return self.ball

