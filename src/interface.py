import pygame
import colors
import settings
from game import Game
from player import Player


class Interface():
    def __init__(self, game: Game):
        self.resolution = settings.resolution
        self.screen = pygame.display.set_mode(self.resolution)
        self.game: Game = game

    def side_bar(self, position):
        pygame.draw.rect(self.screen, colors.brown, (position,
                         self.resolution[1]/25+20, self.resolution[0]/16, self.resolution[1]))
        padding = 5
        position += 5
        h_pos = padding + self.resolution[1]/25+20

        for i in range(8):
            pygame.draw.rect(self.screen, colors.light_brown, (position, h_pos,
                             self.resolution[0]/16 - 2 * padding, self.resolution[0]/16 - 2 * padding), border_radius=5)
            h_pos += padding + self.resolution[0]/16 - 2 * padding

    def display_interface(self):
        self.screen.fill(colors.green)
        self.draw_middle_line()

        self.draw_status_bar()
        self.side_bar(0)
        self.side_bar(self.resolution[0] - self.resolution[0]/16)

    def draw_middle_line(self):
        pygame.draw.line(self.screen, colors.brown,
                         (self.resolution[0]/2, 0), (self.resolution[0]/2, self.resolution[1]), 30)
        pygame.draw.line(self.screen, colors.dark_brown,
                         (self.resolution[0]/2, 0), (self.resolution[0]/2, self.resolution[1]), 24)

    def draw_status_bar(self):
        pygame.draw.rect(self.screen, colors.dark_brown,
                         (0, 0, self.resolution[0], self.resolution[1]/25+20))

        horizontal_padding = 5
        bar_width = self.resolution[0] * 3/7

        self.draw_health_bar(self.game.p1, horizontal_padding, bar_width)

        position = self.resolution[0] - horizontal_padding - bar_width
        self.draw_health_bar(self.game.p2, position, bar_width, reversed=True)

        width = self.resolution[0] - (bar_width +
                                      horizontal_padding) * 2 - 2 * horizontal_padding
        position = bar_width + 2 * horizontal_padding
        self.draw_middle_bar(position, width)

    def draw_middle_bar(self, position, width):
        pygame.draw.rect(self.screen, colors.brown, (position, 10,
                         width, self.resolution[1]/25), border_radius=255)

        font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 15)
        font.set_bold(True)
        text_surface = font.render('Round 1/40', True, (255, 255, 255))
        text_position = text_surface.get_rect(
            center=(self.resolution[0]//2, 10 + self.resolution[1]/50))
        self.screen.blit(text_surface, text_position)

    def draw_health_bar(self, player: Player, position, bar_width, reversed=False):
        upper_padding = 10
        bars_height = self.resolution[1]/25

        color = self.get_health_bar_color(player.health)
        pygame.draw.rect(self.screen, colors.brown, (position, upper_padding,
                         bar_width, bars_height), border_radius=255)

        pygame.draw.rect(self.screen, color, (position + 5, upper_padding+3,
                         (bar_width-10) * (player.health/100), bars_height-6), border_radius=255)

        font = pygame.font.Font('assets/fonts/PressStart2P-Regular.ttf', 15)
        font.set_bold(True)
        name = player.name
        health = f"{player.health}HP"

        text_surface = font.render(
            health if reversed else name, True, (255, 255, 255))
        text_position = text_surface.get_rect(
            center=(position, 10 + self.resolution[1]/50))
        text_position.left = position + 10
        self.screen.blit(text_surface, text_position)

        text_surface = font.render(
            name if reversed else health, True, (255, 255, 255))
        text_position = text_surface.get_rect(
            center=(position, 10 + self.resolution[1]/50))
        text_position.right = position + bar_width - 10
        self.screen.blit(text_surface, text_position)

    def get_health_bar_color(self, health) -> tuple:
        if health > 80:
            r = colors.green[0]
            g = colors.green[1]
            b = colors.green[2]
        elif health > 60:
            r = colors.yellow[0] + (colors.green[0] -
                                    colors.yellow[0]) * (health-60)/20
            g = colors.yellow[1] + (colors.green[1] -
                                    colors.yellow[1]) * (health-60)/20
            b = colors.yellow[2] + (colors.green[2] -
                                    colors.yellow[2]) * (health-60)/20
        elif health > 40:
            r = colors.yellow[0]
            g = colors.yellow[1]
            b = colors.yellow[2]
        elif health > 20:
            r = colors.red[0] + (colors.yellow[0] -
                                 colors.red[0]) * (health-20)/20
            g = colors.red[1] + (colors.yellow[1] -
                                 colors.red[1]) * (health-20)/20
            b = colors.red[2] + (colors.yellow[2] -
                                 colors.red[2]) * (health-20)/20
        else:
            r = colors.red[0]
            g = colors.red[1]
            b = colors.red[2]
        return (r, g, b)
