class Gamestats:
    """Class for calculating the statistics"""
    def __init__(self, ai_game):
        self.setting = ai_game.setting
        self.reset_stats()

    """resetting the statistics after running the main file."""
    def reset_stats(self):
        self.ship_left = self.setting.ship_limit  
        self.score = 0  