import pygame


class Character:
    def __init__(self, spellBook):
        self.curBlock = ""
        self.health = 3
        self.rect = pygame.Rect((450, 350, 80, 100))
        self.spellBook = spellBook
        self.curLetter = 0
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        #health bs
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((5), 5, 50, 50))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((105), 5, 50, 50))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((205), 5, 50, 50))
        for i in range(self.health):
            pygame.draw.rect(surface, (255,0,0), pygame.Rect((i*100+5),5,50,50))

