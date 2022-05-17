import pygame


class Player:
    def __init__(self, position):
        self.origin_position = position
        self._x, self._y = position
        self._origin_pacman = pygame.image.load("asset/player.svg")
        self._pacman = self._origin_pacman

    def move_to_origin(self):
        self._x, self._y = self.origin_position

    def move_up(self, tiles):
        if tiles[self._y - 1][self._x] != 0:
            self._y -= 1
            self.rotate(90)

    def move_down(self, tiles):
        if tiles[self._y + 1][self._x] != 0:
            self._y += 1
            self.rotate(270)

    def move_left(self, tiles):
        if tiles[self._y][self._x - 1] != 0:
            self._x -= 1
            self.rotate(180)

    def move_right(self, tiles):
        if tiles[self._y][self._x + 1] != 0:
            self._x += 1
            self.rotate(0)

    def rotate(self, angle):
        self._pacman = pygame.transform.rotate(self._origin_pacman, angle)

    def get_position(self):
        return self._y, self._x

    def get_image(self):
        return self._pacman

    def draw(self, display, environment):
        environment.draw_image(display, self._y, self._x, self._pacman)

    def set_position(self, position):
        (self._y, self._x) = position
