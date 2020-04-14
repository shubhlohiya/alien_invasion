import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """A class to represent an alien in the fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.png')
        self.image = pygame.transform.scale(self.image, self.settings.alien_size)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Returns True if alien is at edge of the screen"""
        
        if self.rect.right >= self.settings.screen_width or self.rect.left <= 0:
            return True


    def update(self):
        """Move the Aliens"""

        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x