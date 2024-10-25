class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (240, 240, 240)

        # ships settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # alien settings
        self.fleet_drop_speed = 5

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the alien points values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 0.5

        # fleet_direction of 1 represents right ; -1 represents left.
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings alien points values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
