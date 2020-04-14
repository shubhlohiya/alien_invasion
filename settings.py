class Settings:

    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 960
        self.screen_height = 540
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.ship_size = (55,50)
        self.ship_speed = 2

        #Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3.5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        #Alien settings
        self.alien_size = (39, 50)  #(50, 64)
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10        
        self.fleet_direction = 1 # 1 - right / -1 - left.

