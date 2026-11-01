import sys
import pygame
from settings import Settings

class Aliensinvasion:
    """This is main class for the game: aliens invasion."""
    def __init__(self):
        """Method to initialize the game."""
        #initialization of the game.
        pygame.init()

        #making the instances of the Clock class.
        self.clock = pygame.time.Clock()
        
        #making the instances of class settings.
        self.setting = Settings()

        #Setting the windows display.
        self.screen = pygame.display.set_mode((self.setting.screen_width,self.setting.screen_height))
        pygame.display.set_caption("Alien invasion")


    def run_game(self):
        """Method to run the game."""
        while True:
           #iterating the event for user's input.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.setting.bg_color)
            #calling the function for changing action in game.
            pygame.display.flip()
            #Making the game to change repeatly for 60 times per second.
            self.clock.tick(60)        

#conditions for running the file directly.
if __name__ == "__main__":
    ai = Aliensinvasion()
    ai.run_game()