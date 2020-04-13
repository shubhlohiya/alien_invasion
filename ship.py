import pygame

class Ship:
	"""A class to manage the ship."""

	def __init__(self, ai_game):
		"""Initialize the ship and set the starting position"""
		self.settings = ai_game.settings
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.png')
		self.image = pygame.transform.scale(self.image, self.settings.ship_size)
		self.rect = self.image.get_rect()

		#Start each new ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		self.x = float(self.rect.x)

		#Movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on the movement flag"""
		if self.moving_right and not(self.rect.right > self.settings.screen_width):
			self.x += self.settings.ship_speed
		if self.moving_left and not(self.rect.left < 0):
			self.x -=  self.settings.ship_speed

		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at its current location """
		self.screen.blit(self.image, self.rect)