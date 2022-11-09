import sys
import os
import pygame.font
import pygame.freetype
import pygame
from random import randrange
from Button import Button
from character import Character
from boss import Boss

# William Swain
# 08.10.2022

pygame.init()

SCREEN_W = 1000
SCREEN_H = 600

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Buckler")
clock = pygame.time.Clock();
FPS = 60


# method for exporting pygame
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# for getting different size fonts
def get_font(size):
    return pygame.font.SysFont("pristina", size)


def play(recovery_time, damage, max_counter, miss_cooldown):
    # one boss for now
    yetiurl = resource_path("assets/images/bosses/yeti/Yeti.png")
    wizardurl = resource_path("assets/images/wizardspritesheet.png")
    yeti_sprite = pygame.image.load(yetiurl).convert_alpha()
    wizard_sprite = pygame.image.load(wizardurl).convert_alpha()
    character = Character(["wesa", "refca", "frazzer", "wewsa", "wasda", "weza", "qwexa"], wizard_sprite)
    tutorial_boss = Boss(1000, max_counter, miss_cooldown, yeti_sprite)
    index = randrange(0, len(character.spellBook))

    # annoying text work
    text = character.spellBook[index]
    font = pygame.freetype.Font(None, 64)
    font.origin = True
    text_surf_rect = font.get_rect("SUPER LONG STRINGq")
    baseline = text_surf_rect.y
    text_surf_rect.center = (400, 300)
    text_surf = pygame.Surface(font.get_rect("SUPER LONG q").size)
    metrics = font.get_metrics(text)
    M_ADV_X = 4

    screen.fill((0, 0, 0))
    tutorial_boss.draw(screen, 150, 550)
    character.draw(screen)
    pygame.display.update()
    pygame.time.delay(1500)  # give the player a second

    running = True
    # main runner loop: reads all events and reacts to them
    while running:
        clock.tick(FPS)
        tutorial_boss.draw(screen, 150, 550)
        character.draw(screen)
        if tutorial_boss.recoveryTime == 0:
            if tutorial_boss.isBossAttacking:
                if tutorial_boss.attackCounter == 0:
                    tutorial_boss.action = 0
                    if tutorial_boss.attackDirection == character.curBlock:
                        print("BLOCKED")
                    else:
                        character.health -= 1
                        if character.health == 0:
                            # death screen and return to main menu
                            character.draw(screen)
                            pygame.display.update()
                            pygame.time.delay(500)
                            screen.fill((140, 0, 0))
                            font = pygame.font.SysFont('pristina', 64)
                            text = font.render('You Died', True, ((255, 0, 0)))
                            death_rec = text.get_rect()
                            death_rec.center = (500, 300)
                            screen.blit(text, death_rec)
                            pygame.display.update()
                            pygame.time.delay(1500)
                            main_menu()

                    tutorial_boss.isBossAttacking = False
                    tutorial_boss.recoveryTime = recovery_time  # currently recovery time

                else:
                    tutorial_boss.attackCounter -= 1
                    if tutorial_boss.attackCounter == 10:  # attacking animation
                        tutorial_boss.action = 3

            else:
                tutorial_boss.checkIfAttacking()
                if tutorial_boss.isBossAttacking:
                    tutorial_boss.getAttackDirection(screen)
        else:
            tutorial_boss.recoveryTime -= 1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # changes block if user presses different direction
                    character.curBlock = "left"
                    character.action = 4
                if event.key == pygame.K_UP:
                    character.curBlock = "up"
                    character.action = 5
                    print(character.curBlock)
                if event.key == pygame.K_RIGHT:
                    character.curBlock = "right"
                    character.action = 1
                    print(character.curBlock)
                if event.unicode == character.spellBook[index][character.curLetter].lower():
                    character.curLetter += 1
                    if character.curLetter >= len(text):
                        tempaction = character.action
                        character.action = 2
                        character.draw(screen)
                        pygame.display.update()
                        pygame.time.delay(200)
                        character.action = tempaction
                        tutorial_boss.health = tutorial_boss.health - len(text) * damage  # balancing needed
                        if tutorial_boss.health <= 0:
                            tutorial_boss.draw(screen, 150, 550)
                            pygame.display.update()
                            pygame.time.delay(500)
                            screen.fill((218, 165, 32))
                            font = pygame.font.SysFont('pristina', 64)
                            text = font.render('You Win', True, ((255, 255, 255)))
                            winrec = text.get_rect()
                            winrec.center = (500, 300)
                            screen.blit(text, winrec)
                            pygame.display.update()
                            pygame.time.delay(1500)
                            main_menu()
                        character.curLetter = 0
                        index = randrange(0, len(character.spellBook))
                        text = character.spellBook[index]
                        metrics = font.get_metrics(text)

            if event.type == pygame.QUIT:
                running = False
        x = 0
        text_surf.fill((0, 0, 0))

        for (idx, (letter, metric)) in enumerate(zip(character.spellBook[index], metrics)):
            if idx == character.curLetter:
                color = 'lightblue'
            elif idx < character.curLetter:
                color = 'yellow'
            else:
                color = 'white'
            font.render_to(text_surf, (x, baseline), letter, color)
            x += metric[M_ADV_X]

        screen.blit(text_surf, text_surf_rect)
        pygame.display.flip()
    main_menu()


# a page for selecting different parameters for the game
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
                    play(250, 40, 120, 300)
                if hard_button.check_input(mouse_pos):
                    play(100, 15, 40, 200)
                if back_button.check_input(mouse_pos):
                    main_menu()
        pygame.display.update()


# quick tutorial page on how to play the game
def controls_page():
    screen.fill((0, 0, 0))
    contr_text = get_font(40).render("The boss will attack in three directions: left, up, and right", True, "#b68f40")
    contr_rect = contr_text.get_rect(center=(500, 100))
    screen.blit(contr_text, contr_rect)
    contr_text = get_font(40).render("Block incoming attacks with the left, up, or right arrow keys", True, "#b68f40")
    contr_rect = contr_text.get_rect(center=(500, 200))
    screen.blit(contr_text, contr_rect)
    contr_text = get_font(40).render("At the same time, type out spells to damage the boss", True, "#b68f40")
    contr_rect = contr_text.get_rect(center=(500, 300))
    screen.blit(contr_text, contr_rect)
    while True:

        mouse_pos = pygame.mouse.get_pos()
        back_button = Button(image=None, pos=(500, 400), text_input="Back", font=get_font(75), color=(255, 0, 0),
                             hover_color=(255, 255, 255))
        back_button.hovering(mouse_pos)
        back_button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(mouse_pos):
                    main_menu()
        pygame.display.update()


# main hub page
def main_menu():
    screen.fill((0, 0, 0))
    while True:
        mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("Buckler", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(500, 100))
        play_button = Button(image=None, pos=(500, 300), text_input="Play", font=get_font(75), color=((255, 0, 0)),
                             hover_color=((255, 255, 255)))
        tutorial_button = Button(image=None, pos=(500, 400), text_input="Controls", font=get_font(75),
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
                    controls_page()
                if quit_button.check_input(mouse_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


main_menu()

pygame.quit()
