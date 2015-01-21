import pygame
import sys
import math
from random import randint 
from classes import *

class GenericMagic(BaseClass):
	List = pygame.sprite.Group()
	def __init__(self, x, y, width, height, image_string):
	BaseClass.__init__(self, x, y, width, height, image_string)
	GenericMagic.List.add(self)

class Fireball(GenericMagic):
	List = pygame.sprite.Group()
	def __init__(self, x, y, width, height, image_string):
		BaseClass.__init__(self, x, y, width, height, image_string)
		Fireball.List.add(self)

	def launch(self, enemyx, enemyy):
	
	def hit(self):
		for monsters in Monster.List:
			#if fireball hits, self.hp - randint(3,5)