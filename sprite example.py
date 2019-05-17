import pygame
import random
import os

WIDTH = 800
HEIGHT = 800
FPS = 10

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0 , 0, 255)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


class Player(pygame.sprite.Sprite):
	# Sprite for the player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder, "monk.png")).convert()
		self.image.set_colorkey(BLACK) 
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH/2, HEIGHT/2)
		self.y_speed = 10

	def update(self):
		self.rect.x += 5
		self.rect.y += self.y_speed
		if self.rect.bottom > HEIGHT - 300:
			self.y_speed = -10
		if self.rect.top < 300:
			self.y_speed = 10
		if self.rect.left > WIDTH:
			self.rect.right = 0

#initialize pygame and create window
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Game loop
running = True

while running:

	# Keep running loop at the right speed
	clock.tick(FPS)

	# process input (events)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Update
	all_sprites.update()

	# Draw/render
	screen.fill(BLACK)
	all_sprites.draw(screen)

	pygame.display.flip()






pygame.quit()
quit()