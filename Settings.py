class Settings():
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen setting
        self.screen_width = 1080
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        #Ship speed settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #How quickly the game speeds up.
        self.speedup_scale = 1.2


        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 5
        self.score_scale = 1.2

        #fleet_direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien points values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= int(self.alien_points * self.score_scale)
