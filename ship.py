import pygame

class Ship:
    """Making the class for ship."""
    def __init__(self, ai_game):
        """method of ship class."""

        #arranging the screen of the main into rectangle.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.setting


        #loading the image of the ship ans making into rectangle format.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #arranging the location of the ship in the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #making the float type to ship image.
        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # conditions for right movement of ship.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.setting.ship_speed
        #condition for left movement of ship.     
        if self.moving_left and self.rect.left > 0:
            self.x -= self.setting.ship_speed    

        #finalizing the float value to ship image.
        self.rect.x = self.x    

    def biltme(self):
        """Method to arrange the location f ship."""
        self.screen.blit(self.image, self.rect)    
