import pygame
from random import randint
import math

class BaseClass(pygame.sprite.Sprite):

	allsprites = pygame.sprite.Group()
	def __init__(self, x, y, width, height, image_string):
		pygame.sprite.Sprite.__init__(self)
		BaseClass.allsprites.add(self)

		self.image = pygame.image.load(image_string)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

		self.width = width
		self.height = height

class Bug(BaseClass):
	List = pygame.sprite.Group()
	def __init__(self, x, y, width, height, image_string):
		BaseClass.__init__(self, x, y, width, height, image_string)
		Bug.List.add(self)
		self.velx = 0
		self.vely = 5
		self.jumping, self.go_down = False, False

	def motion(self, SCREENWIDTH, SCREENHEIGHT):

		predicted_locationx = self.rect.x + self.velx
		predicted_locationy = self.rect.y + self.vely

		if predicted_locationx < 0:
			self.velx = 0
		elif predicted_locationx + self.width > SCREENWIDTH:
			self.velx = 0
		
		self.rect.x += self.velx

		self.__jump(SCREENHEIGHT)

	def __jump(self, SCREENHEIGHT):

		max_jump = 40

		if self.jumping:

			if self.rect.y < max_jump:
				self.go_down = True



			if self.go_down:
				self.rect.y += self.vely
				predicted_location = self.rect.y + self.vely

				if predicted_location + self.height > SCREENHEIGHT:
					self.jumping = False
					self.go_down = False
			else: 
				self.rect.y -= self.vely

class Monster(BaseClass):
	List = pygame.sprite.Group()
	def __init__(self, x, y, width, height, image_string):
		BaseClass.__init__(self, x, y, width, height, image_string)
		Monster.List.add(self)
		self.velx = randint(2,5)
		self.amplitude = randint(20, 140)
		self.period = randint(4,5) / 100.0

	def fly(self, SCREENWIDTH):
		if  self.rect.x + self.width > SCREENWIDTH or self.rect.x < 0:
			self.image = pygame.transform.flip( self.image, True, False)
			self.velx = -self.velx 
		self.rect.x += self.velx
		#sine function
		self.rect.y = self.amplitude * math.sin(self.period * self.rect.x) + 140


	@staticmethod
	def movement(SCREENWIDTH):
		for monster in Monster.List:
			monster.fly(SCREENWIDTH)
			




