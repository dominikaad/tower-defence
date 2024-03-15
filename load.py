import pygame
from script import load_image
# _image = load_image('image/fon')
fon_image = pygame.image.load('image/tile map/bush_tile 1.png').convert_alpha()
grass_image = pygame.image.load('image/tile map/grass_tile_1.png').convert_alpha()
bush_tower_image = pygame.image.load('image/tile map/bush_tile_tower.png').convert_alpha()
left_image = pygame.image.load('image/tile map/left.png').convert_alpha()
right_image = pygame.image.load('image/tile map/right.png').convert_alpha()
top_image = pygame.image.load('image/tile map/top.png').convert_alpha()
bottom_image = pygame.image.load('image/tile map/bottom.png').convert_alpha()
enemy_image = pygame.image.load('image/enemy/right.png').convert_alpha()
panel_image = pygame.image.load('image/panel.jpg').convert_alpha()