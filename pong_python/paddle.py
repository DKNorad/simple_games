import pygame
from pygame.rect import Rect, RectType
from game_object import GameObject
from pong_python.ball import Ball


class Paddle(GameObject):
    def __init__(self, x_pos, y_pos, width: int, height: int, speed: int, color, field, difficulty: str = "normal",
                 ball_obj: Ball = None):
        super().__init__(x_pos, y_pos, color, field)
        self.width = width
        self.height = height
        self.field_width = self.field.get_width()
        self.field_height = self.field.get_height()
        self.speed = speed
        self.is_start = True
        self.ball_obj = ball_obj
        self.ai_difficulty = difficulty

        self.paddleRect = pygame.Rect(x_pos, y_pos, width, height)
        self.paddle = pygame.draw.rect(self.field, self.color, self.paddleRect)

    def get_paddle_center_pos(self) -> int:
        return self.y_pos + self.height // 2

    def update(self):
        self.paddle = pygame.draw.rect(self.field, self.color, self.paddleRect)

    def move(self):
        if (not (self.paddle.top + self.y_vel <= 0) and
                not (self.paddle.bottom + self.y_vel > self.field_height)):
            self.y_pos += self.speed * self.y_vel

        self.paddleRect = (self.x_pos, self.y_pos, self.width, self.height)

    def get_rect(self) -> Rect | RectType:
        return self.paddle

    def set_difficulty(self):
        if self.ai_difficulty == "Easy":
            self.speed -= 3
        elif self.ai_difficulty == "Normal":
            pass
        elif self.ai_difficulty == "Hard":
            self.speed += 2
        self.is_start = False

    def cpu_ai(self):
        if self.is_start:
            self.set_difficulty()

        if self.ai_difficulty == "Impossible":
            self.y_pos = self.ball_obj.y_pos - self.height // 2
        else:
            if self.ball_obj.x_pos >= self.field_width // 2 and self.ball_obj.x_vel > 0:
                if self.ball_obj.y_pos >= self.get_paddle_center_pos() + self.height / 4:
                    self.y_vel = 1
                elif self.ball_obj.y_pos <= self.get_paddle_center_pos() - self.height / 4:
                    self.y_vel = -1
                else:
                    self.y_vel = 0
            else:
                if self.get_paddle_center_pos() > self.field_height // 2:
                    self.y_vel = -1
                elif self.get_paddle_center_pos() < self.field_height // 2:
                    self.y_vel = 1
                else:
                    self.y_vel = 0
            self.move()
