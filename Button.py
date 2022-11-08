# William Swain
# 08.10.2022
# Button class to redirect user to different pages
class Button:
    def __init__(self, image, pos, text_input, font, color, hover_color):
        self.image = image
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    # draws button on screen
    def update(self, surface):
        if self.image is not None:
            surface.blit(self.image, self.rect)
        surface.blit(self.text, self.text_rect)

    # if click is detected, checks if it was on this button
    def check_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    # changes color if mouse is hovering over button
    def hovering(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hover_color)
        else:
            self.text = self.font.render(self.text_input, True, self.color)
