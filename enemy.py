import pygame


class Enemy:
    def __init__(self, position):
        self._x, self._y = position
        self._ghost = pygame.image.load("asset/ghost.svg")

    def move_up(self):
        self._y -= 1

    def move_down(self):
        self._y += 1

    def move_left(self):
        self._x -= 1

    def move_right(self):
        self._x += 1

    def set_position(self, position):
        (self._x, self._y) = position

    def get_position(self):
        return self._x, self._y

    def get_image(self):
        return self._ghost

    def draw(self, environment):
        environment.draw_image(self._x, self._y, self._ghost)
