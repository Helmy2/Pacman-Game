import pygame

from main import TILE_SIZE, WHITE, BLACK, GREEN, DISPLAY, RED


class Environment:
    def __init__(self, tiles):
        self.tiles = tiles
        self.font = pygame.font.Font(None, TILE_SIZE)

    def draw_map(self):
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                tile = self.tiles[i][j]
                if tile == 1:
                    self.draw_square(i, j, WHITE)
                elif tile == 0:
                    self.draw_square(i, j, BLACK)

    def draw_score(self, score):
        text = self.font.render("Score: " + str(score), True, GREEN)
        DISPLAY.blit(text, [TILE_SIZE, 10])

    @staticmethod
    def draw_square(x, y, color):
        pygame.draw.rect(DISPLAY, color, (y * TILE_SIZE, x * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def draw_dots(self, dots):
        for (i, j) in dots:
            self.draw_dot(i, j, RED)

    @staticmethod
    def draw_dot(x, y, color):
        pygame.draw.circle(DISPLAY, color, [y * TILE_SIZE + TILE_SIZE * .5, x * TILE_SIZE + TILE_SIZE * .5],
                           TILE_SIZE * .1, 0)

    @staticmethod
    def draw_image(x, y, image):
        DISPLAY.blit(image, (y * TILE_SIZE, x * TILE_SIZE))
