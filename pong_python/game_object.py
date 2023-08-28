class GameObject:
    def __init__(self, x_pos, y_pos, color, field):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.field = field
        self.y_vel = 0
        self.x_vel = 0
