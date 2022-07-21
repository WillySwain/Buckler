from random import randrange
import pygame.freetype
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
tutorialBoss = Boss(4)
defaultCharacter = Character(["slam", "slice", "bash"])
index = randrange(0, 3)
text = defaultCharacter.spellBook[index]
font = pygame.freetype.Font(None, 64)
font.origin = True
text_surf_rect = font.get_rect(text)
baseline = text_surf_rect.y
text_surf = pygame.Surface(text_surf_rect.size)
metrics = font.get_metrics(text)

running = True
M_ADV_X = 4
while running:
    clock.tick(FPS)
    tutorialBoss.draw(screen)
    defaultCharacter.draw(screen)
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
            if event.unicode == defaultCharacter.spellBook[index][defaultCharacter.curLetter].lower():
                defaultCharacter.curLetter += 1
                if defaultCharacter.curLetter>=len(text):
                    defaultCharacter.curLetter = 0
                    index = randrange(0, 3)
                    text = defaultCharacter.spellBook[index]
                    text_surf_rect = font.get_rect(text)
                    baseline = text_surf_rect.y
                    text_surf = pygame.Surface(text_surf_rect.size)
                    metrics = font.get_metrics(text)

        if event.type == pygame.QUIT:
            running = False
    x = 0
    text_surf.fill((0, 0, 0))
    for (idx, (letter, metric)) in enumerate(zip(defaultCharacter.spellBook[index], metrics)):
        if idx == defaultCharacter.curLetter:
            color = 'lightblue'
        elif idx < defaultCharacter.curLetter:
            color = 'lightgrey'
        else:
            color = 'white'
        font.render_to(text_surf, (x, baseline), letter, color)
        x += metric[M_ADV_X]

    screen.blit(text_surf, text_surf_rect)
    pygame.display.update()

pygame.quit()
