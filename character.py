import pygame


class Character:
    def __init__(self, spellBook):
        self.curBlock = ""
        self.health = 5
        self.rect = pygame.Rect((450, 350, 80, 100))
        self.spellBook = spellBook
        self.curLetter = 0
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

