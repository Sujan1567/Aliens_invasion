import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from time import sleep
from game_stats import Gamestats
from alien import Alien
from button import Button

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

        #creating the instance of the Gamestats
        self.stats = Gamestats(self)

        #creating the active flag.
        self.game_status = False

        #calling the instance of the ship class.
        self.ship = Ship(self)

        #making the group of the bullets.
        self.bullets = pygame.sprite.Group()

        #making the group of the ships.
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.play_button = Button(self, "play")


    def run_game(self):
        """Method to run the game."""
        while True:
           #iterating the event for user's input.
            self._check_events()

            if self.game_status:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
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

        self._check_bullets_alien_collision()        

      
    def _check_bullets_alien_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)   
        
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()  


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

    def _update_aliens(self):
        """updating the position of the alien"""
        self._check_fleet_edges()
        self.aliens.update() 

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()  

        self._check_aliens_bottom()      
                    
    
    def _create_alien(self, x_position,y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1 

    def _ship_hit(self):
        if self.stats.ship_left > 0:
            """function for collisions of the ship and aliens."""
            self.stats.ship_left -= 1

            #emptying the bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            #creating the fleet and moving ship to center.
            self._create_fleet()
            self.ship.center_ship()

            #pausing the game.
            sleep(0.5) 
        else:
            self.game_status = False    


    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.setting.screen_height:
                self._ship_hit()
                break                  
    

    

    def _update_screen(self):
        self.screen.fill(self.setting.bg_color)  
        #taking the numbers of bullet from given instance.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.biltme()  
        self.bullets.update()
        self.aliens.draw(self.screen)

        if not self.game_status:
            self.play_button.draw_button()
        pygame.display.flip()        

#conditions for running the file directly.
if __name__ == "__main__":
    ai = Aliensinvasion()
    ai.run_game()