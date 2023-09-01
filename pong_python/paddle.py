import pygame
from game_object import GameObject


class Paddle(GameObject):
    def __init__(self, x_pos, y_pos, width, height, speed, color, field, difficulty="normal", ball_obj=None):
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

    def get_paddle_center_pos(self):
        return self.y_pos + self.height // 2

    def update(self):
        self.paddle = pygame.draw.rect(self.field, self.color, self.paddleRect)

    def move(self):
        if (not (self.paddle.top + self.y_vel <= 0) and
                not (self.paddle.bottom + self.y_vel > self.field_height)):
            self.y_pos += self.speed * self.y_vel

        self.paddleRect = (self.x_pos, self.y_pos, self.width, self.height)

    def get_rect(self):
        return self.paddle

    def cpu_ai(self):
        if self.ai_difficulty == 4:
            self.y_pos = self.ball_obj.y_pos - self.height // 2 + 5
        elif self.is_start:
            if self.ai_difficulty == 1:
                self.speed -= 3
            elif self.ai_difficulty == 2:
                pass
            elif self.ai_difficulty == 3:
                self.speed += 2
            self.is_start = False
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
