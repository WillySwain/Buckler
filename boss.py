import pygame
from random import randrange


class Boss:
    def __init__(self, maxHealth, maxCounter,miss_cooldown):

        self.rect = pygame.Rect((600, 100, 80, 100))
        self.miss_cooldown = miss_cooldown
        self.recoveryTime = 0
        self.health = maxHealth
        self.maxHealth = maxHealth
        self.attackCounter = 0
        self.maxCounter = maxCounter
        self.isBossAttacking = False
        self.attackDirection = "up"

    def draw(self, surface,x ,y):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        ratio = self.health / self.maxHealth
        pygame.draw.rect(surface, (80, 80, 80), (x - 2, y - 2, 704, 19))
        pygame.draw.rect(surface, (40, 20, 20), (x, y, 700, 15))
        pygame.draw.rect(surface, (139, 0, 0), (x, y, 700 * ratio, 15))

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
        self.attackCounter = self.maxCounter

    def checkIfAttacking(self):
        attackRoll = randrange(0, 3)
        if attackRoll == 1:
            self.isBossAttacking = True
        else:
            pygame.time.delay(self.miss_cooldown)
            self.isBossAttacking = False
