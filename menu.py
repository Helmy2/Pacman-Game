import pygame

from utilities import BLACK, WIDTH, HEIGHT


class Menu:
    state = 0

    def __init__(self, items, font_color=(0, 0, 0), select_color=(255, 0, 0), ttf_font=None, font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font, font_size)

    def display_frame(self, display):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item, True, self.select_color)
            else:
                label = self.font.render(item, True, self.font_color)

            width = label.get_width()
            height = label.get_height()

            pos_x = (WIDTH * 0.5) - (width * 0.5)
            # t_h: total height of text block
            t_h = len(self.items) * height
            pos_y = (HEIGHT * 0.5) - (t_h * 0.5) + (index * height)

            display.blit(label, (pos_x, pos_y))

    def display_game_over(self, display):
        display.fill(BLACK)
        label = self.font.render("Game over", True, self.select_color)
        width = label.get_width()
        height = label.get_height()
        pos_x = (WIDTH * .5) - (width * .5)
        # t_h: total height of text block
        t_h = len(self.items) * height
        pos_y = (HEIGHT * .5) - (t_h * .5)
        display.blit(label, (pos_x, pos_y))

    def event_handler(self, e):
        if e.key == pygame.K_RETURN:
            if self.state == 0:
                return 0
            if self.state == 1:
                return 1
        if e.key == pygame.K_UP:
            if self.state == 0:
                self.state = 1
            else:
                self.state = 0
        if e.key == pygame.K_DOWN:
            if self.state == 0:
                self.state = 1
            else:
                self.state = 0
