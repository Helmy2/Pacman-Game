import pygame as pygame

from enemy import Enemy
from enviroment import Environment
from player import Player
from utilities import bfs


class Game:
    def __init__(self, tiles, pacman_position):
        self.score = 0
        self.tiles = tiles
        self.environment = Environment(tiles)
        self.player = Player(pacman_position)
        self.enemy = Enemy((15, 15))
        self.dots = self.get_dots_group()
        self.pacman_sound = pygame.mixer.Sound("asset/pacman_sound.ogg")

        self.x = 0
        self.game_over_sound = pygame.mixer.Sound("asset/game_over_sound.ogg")

    def update(self):
        self.environment.draw_map()
        self.environment.draw_dots(self.dots)
        self.environment.draw_score(self.score)

        (x, y) = self.player.get_position()

        self.player.draw(self.environment)
        if (x, y) in self.dots:
            self.score += 1
            self.dots.remove((x, y))
            self.pacman_sound.play()
        self.enemy.draw(self.environment)
        self.update_enemy()

    def get_dots_group(self):
        dots = []
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] == 1 and (i, j) != self.player.get_position():
                    dots.append((i, j))
        return dots

    def move(self, e):

        if e.key == pygame.K_RIGHT:
            self.player.move_right(self.tiles)
        if e.key == pygame.K_LEFT:
            self.player.move_left(self.tiles)
        if e.key == pygame.K_UP:
            self.player.move_up(self.tiles)
        if e.key == pygame.K_DOWN:
            self.player.move_down(self.tiles)

    def is_game_over(self):
        return self.player.get_position() == self.enemy.get_position()

    def update_enemy(self):
        self.x += 1
        if self.x == 10:
            self.x = 0
            move_list = bfs(self.tiles, self.enemy.get_position(), self.player.get_position())
            if len(move_list) > 1:
                self.enemy.set_position(move_list[1])
