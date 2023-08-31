from game_object import GameObject


class Score(GameObject):
    def __init__(self, font, color, field, x_pos, y_pos):
        super().__init__(x_pos, y_pos, color, field)
        self.font = font
        self.p1_score = 0
        self.p2_score = 0

        self.p1_points = None
        self.cpu_points = None

    def update(self):
        self.p1_points = self.font.render(str(self.p1_score), True, self.color, None)
        self.cpu_points = self.font.render(str(self.p2_score), True, self.color, None)

        self.field.blit(self.p1_points, self.p1_points.get_rect(topright=(self.x_pos / 2 + 50, 20)))
        self.field.blit(self.cpu_points, self.cpu_points.get_rect(topleft=(self.x_pos / 2 - 50, 20)))
