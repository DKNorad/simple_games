import pygame
from pygame.rect import Rect, RectType
from game_object import GameObject
from random import randint
from paddle import Paddle


class Ball(GameObject):
    MAX_Y_VEL = 5

    def __init__(self, x_pos, y_pos, radius: int, color, field, p1_paddle: Paddle = None, cpu_paddle: Paddle = None):
        super().__init__(x_pos, y_pos, color, field)
        self.center = (x_pos, y_pos)
        self.field_width = x_pos * 2
        self.field_height = y_pos * 2
        self.radius = radius
        self.hits = 0
        self.default_x_vel = 9
        self.x_vel = self.default_x_vel
        self.p1_paddle = p1_paddle
        self.cpu_paddle = cpu_paddle

        self.is_initial = True
        self.ball = pygame.draw.circle(self.field, self.color, (self.x_pos, self.y_pos), self.radius)

    def calculate_velocity(self, side: str) -> float:
        if side == "left":
            _paddle_middle_y = self.p1_paddle.y_pos + self.p1_paddle.height / 2
            _paddle_height = self.p1_paddle.height
        else:
            _paddle_middle_y = self.cpu_paddle.y_pos + self.cpu_paddle.height / 2
            _paddle_height = self.cpu_paddle.height

        difference_with_ball = _paddle_middle_y - self.y_pos

        vel_reduction = _paddle_height / 2 / self.MAX_Y_VEL
        y_vel = difference_with_ball / vel_reduction

        return y_vel

    def handle_collision(self) -> None:
        # Handle ball collision to top and bottom walls.
        if self.y_pos - self.radius <= 0:
            self.y_vel *= -1
        elif self.y_pos + self.radius >= self.field.get_height():
            self.y_vel *= -1

        # Handle ball collision to the player paddle on the left.
        if self.x_vel < 0:
            if self.p1_paddle.y_pos <= self.y_pos <= self.p1_paddle.y_pos + self.p1_paddle.height:
                if self.p1_paddle.x_pos + self.p1_paddle.width >= self.x_pos - self.radius:
                    self.hit(self.calculate_velocity("left"))

        # Handle ball collision to the CPU paddle on the right.
        if self.x_vel > 0:
            if self.cpu_paddle.y_pos <= self.y_pos <= self.cpu_paddle.y_pos + self.cpu_paddle.height:
                if self.cpu_paddle.x_pos <= self.x_pos + self.radius:
                    self.hit(self.calculate_velocity("right"))

    def update(self) -> None:
        self.ball = pygame.draw.circle(self.field, self.color, (self.x_pos, self.y_pos), self.radius)

    def handle_movement(self) -> None:
        if self.is_initial:
            self.x_vel = self.default_x_vel - 3
            self.y_vel = randint(-self.MAX_Y_VEL, self.MAX_Y_VEL)
            self.is_initial = False
        elif self.hits == 1:
            self.x_vel = self.default_x_vel

        self.y_pos += self.y_vel
        self.x_pos += self.x_vel

    def hit(self, y_vel: float) -> None:
        self.hits += 1
        self.x_vel *= -1
        self.y_vel = -1 * y_vel

        # Increase the X speed every 5 hits.
        if self.hits % 5 == 0:
            self.x_vel *= 1.05

    def reset(self) -> None:
        self.is_initial = True
        self.x_pos = self.center[0]
        self.y_pos = self.center[1]
        self.hits = 0

    def get_rect(self) -> Rect | RectType:
        return self.ball

