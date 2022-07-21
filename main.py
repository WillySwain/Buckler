from random import randrange

import pygame
from character import Character
from boss import Boss

pygame.init()

SCREEN_W = 1000
SCREEN_H = 600

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Buckler")
clock = pygame.time.Clock();
FPS = 60
font = pygame.font.SysFont('pristina', 64)
tutorialBoss = Boss(4)
defaultCharacter = Character(["slam", "bam", "blow"])
running = True
index = randrange(0, 3)
text = font.render(defaultCharacter.spellBook[index],True,(234,221,202))
textRect = text.get_rect()
while running:
    clock.tick(FPS)
    tutorialBoss.draw(screen)
    defaultCharacter.draw(screen)
    screen.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                defaultCharacter.curBlock = "left"
                print(defaultCharacter.curBlock)
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(700, 400, 60, 60))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(800, 300, 60, 60))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(900, 400, 60, 60))
            if event.key == pygame.K_UP:
                defaultCharacter.curBlock = "up"
                print(defaultCharacter.curBlock)
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(800, 300, 60, 60))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(700, 400, 60, 60))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(900, 400, 60, 60))
            if event.key == pygame.K_RIGHT:
                defaultCharacter.curBlock = "right"
                print(defaultCharacter.curBlock)
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(900, 400, 60, 60))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(800, 300, 60, 60))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(700, 400, 60, 60))

        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
