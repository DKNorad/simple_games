import math

import pygame
from game_object import GameObject
from random import choice


class Ball(GameObject):
    MAX_VEL = 5

    def __init__(self, x_pos, y_pos, radius, speed, color, field):
        super().__init__(x_pos, y_pos, color, field)
        self.center = (x_pos, y_pos)
        self.width = x_pos * 2
        self.height = y_pos * 2
        self.radius = radius
        self.speed = speed
        self.default_speed = speed
        self.hits = 0

        self.is_initial = True
        self.ball = pygame.draw.circle(self.field, self.color, (self.x_pos, self.y_pos), self.radius)

    def update(self):
        self.ball = pygame.draw.circle(self.field, self.color, (self.x_pos, self.y_pos), self.radius)

    def handle_movement(self):
        if self.is_initial:
            self.y_vel = choice([-1, 1])
            self.x_vel = self.MAX_VEL
            self.is_initial = False

        self.y_pos += self.y_vel
        self.x_pos += self.x_vel

    def hit(self, y_vel):
        self.hits += 1

        if self.hits == 1:
            self.speed *= 1.4

        self.x_vel *= -1
        self.y_vel *= y_vel

    def reset(self):
        self.is_initial = True
        self.x_pos = self.center[0]
        self.y_pos = self.center[1]
        self.hits = 0
        self.speed = self.default_speed

    def calculate_trajectory(self, begin_y, angle):
        x_speed = math.cos(angle)  # calculate the relative x of the angle
        y_speed = math.sin(angle)  # calculate the relative y of the angle

        straight_pos = begin_y + self.width * y_speed / x_speed
        # this is the final position if the ball wouldn't change direction

        final_pos = abs(straight_pos) % (2 * self.height)
        # a negative result just of straight_pos means it bounces one additional time
        # but has no effect on the result.
        # (that's why abs(straight_pos) instead of just straight_pos)
        # if the result is 2 * height it means that the ball has bounced twice
        # and has returned to y position 0.

        if final_pos > self.height:
            final_pos = 2 * self.height - final_pos
        # if final_pos > height this means that the ball has bounced once and
        # the final position is the remainder to 2 * height.

        return final_pos

    def get_rect(self):
        return self.ball

