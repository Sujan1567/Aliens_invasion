import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        #calling the instance of the ship class.
        self.ship = Ship(self)

        #making the group of the bullets.
        self.bullets = pygame.sprite.Group()

        #making the group of the ships.
        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Method to run the game."""
        while True:
           #iterating the event for user's input.
            self._check_events()
            self.ship.update()

            self._update_bullets()
            self._update_screen()

            #Making the game to change repeatly for 60 times per second.
            self.clock.tick(60)     

    def _check_events(self):
        for event in pygame.event.get():
            #exit from the game.
            if event.type == pygame.QUIT:
                sys.exit()
            #pressing the down the key.    
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            #pressing up the key.         
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                  

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()    
        elif event.key == pygame.K_q:
            sys.exit()    

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False  

    def _fire_bullets(self):
        if len(self.bullets) < self.setting.bullet_allowed:
         new_bullets = Bullet(self)
         self.bullets.add(new_bullets)   

    def _update_bullets(self):
        self.bullets.update()

         #for deleting the bullet, which pass from screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """method for making instance of alien."""
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size


        current_x,current_y = alien_width,alien_height
        while (current_y < self.setting.screen_height - 3 * alien_height):
            while (current_x < self.setting.screen_width - 2 * alien_width):
                self._create_alien(current_x,current_y)
            
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height    
                    
    
    def _create_alien(self, x_position,y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)  
        #taking the numbers of bullet from given instance.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.biltme()  
        self.bullets.update()
        self.aliens.draw(self.screen)
        pygame.display.flip()        

#conditions for running the file directly.
if __name__ == "__main__":
    ai = Aliensinvasion()
    ai.run_game()