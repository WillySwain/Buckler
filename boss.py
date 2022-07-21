import pygame
from random import randrange


class Boss:
    def __init__(self, maxHealth):

        self.rect = pygame.Rect((600, 100, 80, 100))
        self.recoveryTime = 0
        self.health = maxHealth
        self.maxHealth = maxHealth
        self.attackCounter = 0
        self.isBossAttacking = False
        self.attackDirection = "up"

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def getAttackDirection(self,surface):
        direction = randrange(0, 3)
        if direction == 0:
            self.attackDirection = "up"
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(800, 250, 60, 20))
        elif direction == 1:
            self.attackDirection = "left"
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(700, 350, 60, 20))
        elif direction == 2:
            self.attackDirection = "right"
            pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(900, 350, 60, 20))
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        self.attackCounter = 100

    def checkIfAttacking(self):
        attackRoll = randrange(0, 3)
        if attackRoll == 1:
            self.isBossAttacking = True
        else:
            self.isBossAttacking = False
