import pygame
import sys

def process(bug):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	keys = pygame.key.get_pressed()

	if keys[pygame.K_d]:
		bug.image = pygame.image.load("./images/cat.png")
		bug.velx = 5
	elif keys[pygame.K_a]:
		bug.image = pygame.image.load("./images/cat_back.png")
		bug.velx = -5
	else:
		bug.velx = 0
	
	if keys[pygame.K_w]:
		bug.jumping = True
