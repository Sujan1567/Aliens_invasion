import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.setting = ai_game.setting

        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        


        self.x = float(self.rect.x)

    def update(self):
        """Moving the alien to the right side."""
        self.x += self.setting.alien_speed
        self.rect.x = self.x    