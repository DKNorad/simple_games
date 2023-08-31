import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, font, color, color_hover, rect, callback, text, outline=None):
        super().__init__()
        self.font = font
        self.base_color = color
        self.hovering_color = color_hover
        self.text = text

        tmp_rect = pygame.Rect(0, 0, *rect.size)

        self.org = self._create_image(color, outline, text, tmp_rect)
        self.hov = self._create_image(color_hover, outline, text, tmp_rect)

        self.image = self.org
        # ...and the rect holds the Rect that defines it position
        self.rect = rect
        self.callback = callback

    def _create_image(self, color, outline, text, rect):
        img = pygame.Surface(rect.size)
        if outline:
            img.fill(outline)
            img.fill(color, rect.inflate(-4, -3))
        else:
            img.fill(color)

        # render the text once here instead of every frame
        if text != '':
            text_surf = self.font.render(text, 1, pygame.Color('black'))
            text_rect = text_surf.get_rect(center=rect.center)
            img.blit(text_surf, text_rect)
        return img

    def update(self, events):
        pos = pygame.mouse.get_pos()
        hit = self.rect.collidepoint(pos)

        self.image = self.hov if hit else self.org
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and hit:
                self.callback(self)
