import pygame
import os
import sys
import random
import time


pygame.init()

game_over = False


width = 800
height = 800

screen = pygame.display.set_mode((width, height))

player_color = (255, 255, 255)
player_pos = [0, 700]
player_size = 50


enemy_size = 50
enemy_pos = [random.randint(0, width-enemy_size), 0]
enemy_color = (255, 0, 0)
enemy_list = [enemy_pos]


def update_enemy_pos(enemy_list):
	for enemy_pos in enemy_list:

		if enemy_pos[1] >= 0 and enemy_pos[1] <=650:
			enemy_pos[1] += 10

		else:
			enemy_pos[1] = 0
			enemy_pos[0] = random.randint(0, width-enemy_size)


def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.02:
		x_pos = random.randint(0, width-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, enemy_color, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def check_collision(enemy_list, player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos, player_pos):
			return True


def detect_collision(enemy_pos, player_pos):
	p_x = player_pos[0]
	p_y = player_pos[1]

	e_x = enemy_pos[0]
	e_y = enemy_pos[1]

	if (e_x > p_x and e_x < p_x+player_size) or (p_x > e_x and p_x < e_x+enemy_size):
		if (p_y > e_y and p_y < e_y+enemy_size) or (e_y > p_y and e_y < p_y+player_size):
			return True


# Main game loop
while not game_over:

	for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.KEYDOWN:
				x = player_pos[0]
				y = player_pos[1]

				if event.key == pygame.K_LEFT:
					x -= 60
					if x<0:
						x = 0

				elif event.key == pygame.K_RIGHT:
					x += 60
					if x>width-player_size:
						x = width-player_size

				player_pos = [x, y]

	screen.fill((0, 0, 0))
	
	draw_enemies(enemy_list)
	drop_enemies(enemy_list)
	update_enemy_pos(enemy_list)
	if check_collision(enemy_list, player_pos):
		game_over = False
		break


	pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))
	

	pygame.display.update()		