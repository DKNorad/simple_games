import pygame
from game_object import GameObject


class Score(GameObject):
    def __init__(self, font, size, color, field, x_pos, y_pos):
        super().__init__(x_pos, y_pos, color, field)
        self.font = font
        self.size = size
        self.p1_score = 0
        self.p2_score = 0

        self.scoreFont = pygame.font.Font(self.font, self.size)
        self.scoreText = self.scoreFont.render(f"Score", True, self.color, None)
        self.scoreTextRect = self.scoreText.get_rect(center=(self.x_pos, self.size))

        self.scorePoints = self.scoreFont.render(f"{self.p1_score} - {self.p2_score}",
                                                 True, self.color, None)

    def update(self):
        self.field.blit(self.scoreText, self.scoreTextRect)
        self.scorePoints = self.scoreFont.render(f"{self.p1_score} - {self.p2_score}",
                                                 True, self.color, None)
        self.field.blit(self.scorePoints, self.get_rect())

    def get_rect(self):
        """Center the points and return as rect object"""
        return self.scorePoints.get_rect(center=(self.x_pos, self.size * 2))
