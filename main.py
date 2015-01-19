import pygame
import sys
from classes import *
from process import *
from magic import *

SCREENWIDTH = 640
SCREENHEIGHT = 360

pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
clock = pygame.time.Clock()
FPS = 24

bug = Bug(0, SCREENHEIGHT-40, 40, 40, './images/cat.png')
background = pygame.image.load('./images/forest.jpg')
monster = Monster(40, 130, 64, 64, './images/monster.png')
monster1 = Monster(40, 130, 64, 64, './images/monster.png')
monster2 = Monster(40, 130, 64, 64, './images/monster.png')
monster3 = Monster(40, 130, 64, 64, './images/monster.png')

while True:
	process(bug)
	
	bug.motion(SCREENWIDTH, SCREENHEIGHT)
	Monster.movement(SCREENWIDTH)


	screen.blit(background, (0,0))
	BaseClass.allsprites.draw(screen)
	pygame.display.flip()
	clock.tick(FPS)