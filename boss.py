import pygame


class Boss:
    def __init__(self):
        self.rect = pygame.Rect((600, 100, 80, 100))

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
