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

tutorialBoss = Boss()
defaultCharacter = Character()
running = True
while running:
    clock.tick(FPS)
    tutorialBoss.draw(screen)
    defaultCharacter.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                defaultCharacter.curBlock = "left"
                print(defaultCharacter.curBlock)
                pygame.draw.rect(screen,(255,255,255) , pygame.Rect(700, 400, 60, 60))
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                defaultCharacter.curBlock = ""
                print(defaultCharacter.curBlock)

        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()
