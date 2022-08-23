import pygame
from random import randrange


class Boss:
    def __init__(self, maxHealth, maxCounter,miss_cooldown,sprite_sheet):
        self.images = self.load_images(sprite_sheet)
        self.action = 0 #0 idle #1:right attack #2:up attack #3 attack hit #4 left attack
        self.image = self.images[self.action]
        self.rect = pygame.Rect((500, 0, 80, 100))
        self.miss_cooldown = miss_cooldown
        self.recoveryTime = 0
        self.health = maxHealth
        self.maxHealth = maxHealth
        self.attackCounter = 0
        self.maxCounter = maxCounter
        self.isBossAttacking = False
        self.attackDirection = "up"

    def load_images(self,sprite_sheet):
        images = []
        for i in range(5):
            tempimage = sprite_sheet.subsurface(i*128,0,128,128)
            images.append(pygame.transform.scale(tempimage,(128*3,128*3)))
        return images
    def draw(self, surface,x ,y):
        pygame.draw.rect(surface, (0,0,0), pygame.Rect(500, 0, 384, 384))
        self.image = self.images[self.action]
        surface.blit(self.image,(self.rect.x,self.rect.y))
        ratio = self.health / self.maxHealth
        pygame.draw.rect(surface, (80, 80, 80), (x - 2, y - 2, 704, 19))
        pygame.draw.rect(surface, (40, 20, 20), (x, y, 700, 15))
        pygame.draw.rect(surface, (139, 0, 0), (x, y, 700 * ratio, 15))

    def getAttackDirection(self,surface):
        direction = randrange(0, 3)
        if direction == 0:
            self.attackDirection = "up"
            self.action=2
            #pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(800, 250, 60, 20))
        elif direction == 1:
            self.attackDirection = "left"
            self.action=4
            #pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(700, 350, 60, 20))
        elif direction == 2:
            self.attackDirection = "right"
            self.action = 1
            #pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(900, 350, 60, 20))
        self.attackCounter = self.maxCounter

    def checkIfAttacking(self):
        attackRoll = randrange(0, 3)
        if attackRoll == 1:
            self.isBossAttacking = True
        else:
            pygame.time.delay(self.miss_cooldown)
            self.isBossAttacking = False
