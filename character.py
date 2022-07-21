import pygame


class Character:
    def __init__(self):
        self.curBlock = ""
        self.rect = pygame.Rect((500, 300, 80, 100))

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

