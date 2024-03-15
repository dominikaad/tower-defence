import pygame
import os
import sys
import random
pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1280
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Aria', 100)
lvl_game = 1
from load import *

timer = 0
def game_lvl():
    global timer
    timer += 1
    if timer / FPS > 1:
        enemy = Player(enemy_image, (0, 565))
        enemy_group.add(enemy)
        timer = 0
    earth_group.draw(sc)
    earth_group.update()
    button_group.draw(sc)
    button_group.update()
    place_tower_group.draw(sc)
    place_tower_group.update()
    enemy_group.draw(sc)
    enemy_group.update()
    panel_group.draw(sc)
    panel_group.update()
    pygame.display.update()
def drawMaps(nameFile):
    maps = []
    source = 'game_lvl/' + str(nameFile)
    with open(source, 'r') as file:
        for i in range(0, 10):
            maps.append(file.readline().replace('\n', '').split(',')[0:-1])
    pos = [0, 0]
    for i in range(0, len(maps)):
        pos[1] = i * 80
        for j in range(0, len(maps[0])):
            pos[0] = 80 * j
            if maps[i][j] == '1':
                bottom_earth = Button(bottom_image, pos, 'bottom')
                button_group.add(bottom_earth)
            elif maps[i][j] == '2':
                fon_earth = Box(fon_image, pos)
                earth_group.add(fon_earth)
            elif maps[i][j] == '3':
                tower_earth = Place_tower(bush_tower_image, pos)
                place_tower_group.add(tower_earth)
            elif maps[i][j] == '4':
                grass_earth = Box(grass_image, pos)
                earth_group.add(grass_earth)
            elif maps[i][j] == '5':
                left_earth = Button(left_image, pos, 'left')
                button_group.add(left_earth)
            elif maps[i][j] == '6':
                right_earth = Button(right_image, pos, 'right')
                button_group.add(right_earth)
            elif maps[i][j] == '7':
                top_earth = Button(top_image, pos, 'top')
                button_group.add(top_earth)



class Button (pygame.sprite.Sprite):
    def __init__(self,image, pos, dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.dir = dir
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Box (pygame.sprite.Sprite):
    def __init__(self,image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Place_tower (pygame.sprite.Sprite):
    def __init__(self,image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
class Player(pygame.sprite.Sprite):
    def __init__(self,image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = 'right'
        self.speedx = 2
        self.speedy = 0
        self.timer = 0

    def move(self):
        if self.dir == 'right':
            self.speedx = 2
            self.speedy = 0
            self.image = pygame.transform.rotate(enemy_image, 0)
        elif self.dir == 'top':
            self.speedx = 0
            self.speedy = -2
            self.image = pygame.transform.rotate(enemy_image, 90)
        elif self.dir == 'left':
            self.speedx = -2
            self.speedy = 0
            self.image = pygame.transform.rotate(enemy_image, 180)
        elif self.dir == 'bottom':
            self.speedx = 0
            self.speedy = 2
            self.image = pygame.transform.rotate(enemy_image, 270)

    def dir_change(self):
        if pygame.sprite.spritecollide(self, button_group, False):
            tile = pygame.sprite.spritecollide(self, button_group, False)[0]
            if abs(self.rect.centerx - tile.rect.centerx)<= 5 and abs(self.rect.centery - tile.rect.centery) <= 5:
                self.dir = tile.dir

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        self.move()
        self.dir_change()


def restart():
    global earth_group, enemy_group, place_tower_group, button_group, panel_group, panel
    earth_group = pygame.sprite.Group()
    button_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    panel_group = pygame.sprite.Group()
    panel = Box(panel_image, (0, 720))
    panel_group.add(panel)
    place_tower_group = pygame.sprite.Group()



restart()
drawMaps('1.txt')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_lvl()
    clock.tick(FPS)