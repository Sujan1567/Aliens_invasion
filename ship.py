import pygame

class Ship:
    """Making the class for ship."""
    def __init__(self, ai_game):
        """method of ship class."""

        #arranging the screen of the main into rectangle.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #loading the image of the ship ans making into rectangle format.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #arranging the location of the ship in the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def biltme(self):
        """Method to arrange the location f ship."""
        self.screen.blit(self.image, self.rect)    
