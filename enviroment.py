import pygame

from utilities import GREEN, RED, TILE_SIZE, WHITE, BLACK


class Environment:
    def __init__(self, tiles):
        self.tiles = tiles
        self.font = pygame.font.Font(None, TILE_SIZE)

    def draw_map(self, display):
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                tile = self.tiles[i][j]
                if tile == 1:
                    self.draw_square(display, i, j, WHITE)
                elif tile == 0:
                    self.draw_square(display, i, j, BLACK)

    def draw_score(self, display, score):
        text = self.font.render("Score: " + str(score), True, GREEN)
        display.blit(text, [TILE_SIZE, 10])

    @staticmethod
    def draw_square(display, x, y, color):
        pygame.draw.rect(display, color, (y * TILE_SIZE, x * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def draw_dots(self, display, dots):
        for (i, j) in dots:
            self.draw_dot(display, i, j, RED)

    @staticmethod
    def draw_dot(display, x, y, color):
        pygame.draw.circle(display, color, [y * TILE_SIZE + TILE_SIZE * .5, x * TILE_SIZE + TILE_SIZE * .5],
                           TILE_SIZE * .1, 0)

    @staticmethod
    def draw_image(display, x, y, image):
        display.blit(image, (y * TILE_SIZE, x * TILE_SIZE))
