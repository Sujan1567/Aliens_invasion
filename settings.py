class Settings:
    """class for managing the settings of game."""
    def __init__(self):
        """method for different settings."""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,120)
        self.bullet_allowed = 3