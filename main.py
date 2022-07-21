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


def draw_boss_health(health, x, y):
    ratio = health / tutorialBoss.maxHealth
    pygame.draw.rect(screen, (80, 80, 80), (x - 2, y - 2, 704, 19))
    pygame.draw.rect(screen, (40, 20, 20), (x, y, 700, 15))
    pygame.draw.rect(screen, (139, 0, 0), (x, y, 700 * ratio, 15))


tutorialBoss = Boss(1000)
defaultCharacter = Character(["slam", "slicer", "bash", "augue incidant tibi"])
index = randrange(0, len(defaultCharacter.spellBook))
text = defaultCharacter.spellBook[index]
font = pygame.freetype.Font(None, 64)
font.origin = True
text_surf_rect = font.get_rect(text)
baseline = text_surf_rect.y
text_surf = pygame.Surface(font.get_rect(defaultCharacter.spellBook[3]).size)
metrics = font.get_metrics(text)
running = True
M_ADV_X = 4
while running:
    clock.tick(FPS)

    draw_boss_health(tutorialBoss.health, 150, 550)
    tutorialBoss.draw(screen)
    defaultCharacter.draw(screen)
    if tutorialBoss.recoveryTime == 0:
        if tutorialBoss.isBossAttacking:
            if tutorialBoss.attackCounter == 0:
                if tutorialBoss.attackDirection == defaultCharacter.curBlock:
                    print("Nice block bruh")
                else:
                    print("you got owned")
                    defaultCharacter.health -= 1
                    print(defaultCharacter.health)
                tutorialBoss.isBossAttacking = False
                tutorialBoss.recoveryTime = 10 #currently recovery time
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(800, 250, 60, 20))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(700, 350, 60, 20))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(900, 350, 60, 20))

            else:
                tutorialBoss.attackCounter -= 1
                if tutorialBoss.attackCounter == 20:
                    if tutorialBoss.attackDirection == "left":
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(700, 350, 60, 20))
                    elif tutorialBoss.attackDirection == "right":
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(900, 350, 60, 20))
                    elif tutorialBoss.attackDirection == "up":
                        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(800, 250, 60, 20))

        else:
            tutorialBoss.checkIfAttacking()
            if tutorialBoss.isBossAttacking:
                tutorialBoss.getAttackDirection(screen)
    else:
        tutorialBoss.recoveryTime -= 1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                defaultCharacter.curBlock = "left"
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
                if defaultCharacter.curLetter >= len(text):
                    tutorialBoss.health = tutorialBoss.health - len(text) * 3  # balancing needed
                    defaultCharacter.curLetter = 0
                    index = randrange(0, len(defaultCharacter.spellBook))
                    text = defaultCharacter.spellBook[index]
                    text_surf_rect = font.get_rect(text)
                    baseline = text_surf_rect.y
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
