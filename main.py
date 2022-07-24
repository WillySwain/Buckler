import sys
from random import randrange

import pygame.font
import pygame.freetype
import pygame

from Button import Button
from character import Character
from boss import Boss

pygame.init()

SCREEN_W = 1000
SCREEN_H = 600

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Buckler")
clock = pygame.time.Clock();
FPS = 60


def get_font(size):
    return pygame.font.SysFont("pristina", size)


def play(difficulty):
    if difficulty == "hard":
        damage = 7
        recoveryTime = 50
        maxCounter = 10
        miss_cooldown = 50
        defaultCharacter = Character(["wasafe", "raslacar", "augue inrcidant tibi", "etwad", "freeasr", "qazxcdews"])

    else:
        damage = 15
        defaultCharacter = Character(["wesa", "refca", "frazzer", "wewsa", "wasda", "weza"])
        recoveryTime = 100
        maxCounter = 40
        miss_cooldown = 200
    tutorialBoss = Boss(1000, maxCounter,miss_cooldown)
    index = randrange(0, len(defaultCharacter.spellBook))

    # annoying text work
    text = defaultCharacter.spellBook[index]
    font = pygame.freetype.Font(None, 64)
    font.origin = True
    text_surf_rect = font.get_rect("SUPER LONG STRINGq")
    baseline = text_surf_rect.y
    text_surf_rect.center = (400, 300)
    text_surf = pygame.Surface(font.get_rect("SUPER LONG q").size)
    metrics = font.get_metrics(text)
    M_ADV_X = 4

    screen.fill((0, 0, 0))
    tutorialBoss.draw(screen, 150, 550)
    defaultCharacter.draw(screen)
    pygame.display.update()
    pygame.time.delay(1500)  # give the player a second

    running = True
    while running:
        clock.tick(FPS)
        tutorialBoss.draw(screen, 150, 550)
        defaultCharacter.draw(screen)
        if tutorialBoss.recoveryTime == 0:
            if tutorialBoss.isBossAttacking:
                if tutorialBoss.attackCounter == 0:
                    if tutorialBoss.attackDirection == defaultCharacter.curBlock:
                        print("BLOCKED")
                    else:
                        defaultCharacter.health -= 1
                        if defaultCharacter.health == 0:
                            # death screen and return to main menu
                            defaultCharacter.draw(screen)
                            pygame.display.update()
                            pygame.time.delay(500)
                            screen.fill((140, 0, 0))
                            font = pygame.font.SysFont('pristina', 64)
                            text = font.render('You Died', True, ((255, 0, 0)))
                            deathrec = text.get_rect()
                            deathrec.center = (500, 300)
                            screen.blit(text, deathrec)
                            pygame.display.update()
                            pygame.time.delay(1500)
                            main_menu()

                    tutorialBoss.isBossAttacking = False
                    tutorialBoss.recoveryTime = recoveryTime  # currently recovery time
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
                        tutorialBoss.health = tutorialBoss.health - len(text) * damage  # balancing needed
                        if tutorialBoss.health <= 0:
                            tutorialBoss.draw(screen,150,550)
                            pygame.display.update()
                            pygame.time.delay(500)
                            screen.fill((218,165,32))
                            font = pygame.font.SysFont('pristina', 64)
                            text = font.render('You Win', True, ((255, 255, 255)))
                            winrec = text.get_rect()
                            winrec.center = (500, 300)
                            screen.blit(text, winrec)
                            pygame.display.update()
                            pygame.time.delay(1500)
                            main_menu()
                        defaultCharacter.curLetter = 0
                        index = randrange(0, len(defaultCharacter.spellBook))
                        text = defaultCharacter.spellBook[index]
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
        pygame.display.flip()
    main_menu()


def select_difficulty():
    screen.fill((0, 0, 0))
    while True:
        mouse_pos = pygame.mouse.get_pos()
        easy_button = Button(image=None, pos=(500, 200), text_input="Easy", font=get_font(75), color=(255, 0, 0),
                             hover_color=(255, 255, 255))
        hard_button = Button(image=None, pos=(500, 300), text_input="Hard", font=get_font(75),
                             color=(255, 0, 0),
                             hover_color=(255, 255, 255))
        back_button = Button(image=None, pos=(500, 400), text_input="Back", font=get_font(75), color=(255, 0, 0),
                             hover_color=(255, 255, 255))
        for button in [easy_button, hard_button, back_button]:
            button.hovering(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.check_input(mouse_pos):
                    play("easy")
                if hard_button.check_input(mouse_pos):
                    play("hard")
                if back_button.check_input(mouse_pos):
                    main_menu()
        pygame.display.update()


def main_menu():
    screen.fill((0, 0, 0))
    while True:
        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("Buckler", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(500, 100))
        play_button = Button(image=None, pos=(500, 300), text_input="Play", font=get_font(75), color=((255, 0, 0)),
                             hover_color=((255, 255, 255)))
        tutorial_button = Button(image=None, pos=(500, 400), text_input="Tutorial", font=get_font(75),
                                 color=(255, 0, 0),
                                 hover_color=(255, 255, 255))
        quit_button = Button(image=None, pos=(500, 500), text_input="Quit", font=get_font(75), color=(255, 0, 0),
                             hover_color=(255, 255, 255))
        screen.blit(menu_text, menu_rect)

        for button in [play_button, tutorial_button, quit_button]:
            button.hovering(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_input(mouse_pos):
                    select_difficulty()
                if tutorial_button.check_input(mouse_pos):
                    print("Coming Soon")
                if quit_button.check_input(mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


main_menu()

pygame.quit()
