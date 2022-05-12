import time

import pygame

from game import Game
from menu import Menu
from utilities import TILES, WHITE, BLACK, HEIGHT, WIDTH

pygame.init()
DISPLAY = pygame.display.set_mode([WIDTH, HEIGHT])

if __name__ == '__main__':
    clock = pygame.time.Clock()
    pygame.display.set_caption("PACMAN")
    game = Game(TILES, (1, 1))
    menu = Menu(("Start", "Exit"), font_color=WHITE, font_size=60)

    running = True
    game_over = True

    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_over:
                    var = menu.event_handler(event)
                    if var == 0:
                        game_over = False
                    if var == 1:
                        running = False
                else:
                    game.move(event)

        DISPLAY.fill(BLACK)
        if game_over:
            game = Game(TILES, (1, 1))
            menu.display_frame(DISPLAY)
        else:
            game.update(DISPLAY)
            game_over = game.is_game_over()
            if game_over == 1 or game_over == 2:
                win = True
                if game_over == 1:
                    win = False
                menu.display_game_over(DISPLAY, game.score, win)
                pygame.display.update()
                time.sleep(2)

        pygame.display.update()

    pygame.quit()
