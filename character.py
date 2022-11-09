import pygame


# William Swain
# 08.10.2022
# character class
class Character:
    def __init__(self, spell_book, sprite_sheet):
        self.images = self.load_images(sprite_sheet)
        self.action = 0  # 0 idle #1:rightblock #2:attack #3 oops frontblock #4 blockleft #5 block up
        self.image = self.images[self.action]
        self.curBlock = ""
        self.health = 5
        self.rect = pygame.Rect((450, 350, 80, 100))
        self.spellBook = spell_book
        self.curLetter = 0

    # parses sprite sheet and gets different frames to load
    def load_images(self, sprite_sheet):
        images = []
        for i in range(7):
            tempimage = sprite_sheet.subsurface(i * 128, 0, 128, 128)
            images.append(pygame.transform.scale(tempimage, (128 * 1.5, 128 * 1.5)))
        return images

    # draws the character and health on the screen
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(450, 320, 192, 192))
        self.image = self.images[self.action]
        surface.blit(self.image, (self.rect.x, self.rect.y))
        # health
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((5), 5, 80, 64))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((105), 5, 80, 64))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((205), 5, 80, 64))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((305), 5, 80, 64))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((405), 5, 80, 64))
        for i in range(self.health):
            surface.blit(self.images[6], (i * 100 - 50, -50))
