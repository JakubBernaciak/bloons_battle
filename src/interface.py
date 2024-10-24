import pygame
import colors


class Interface():
    def __init__(self, resolution: tuple):
        self.resolution = resolution
        self.screen = pygame.display.set_mode(self.resolution)

    def display_interface(self, player_one_health):
        self.screen.fill(colors.green)
        self.draw_middle_line()
        self.draw_status_bar(player_one_health)

    def draw_middle_line(self):
        pygame.draw.line(self.screen, colors.black,
                         (self.resolution[0]/2, 0), (self.resolution[0]/2, self.resolution[1]), 30)
        pygame.draw.line(self.screen, colors.grey,
                         (self.resolution[0]/2, 0), (self.resolution[0]/2, self.resolution[1]), 24)

    def draw_status_bar(self, player_one_health):
        pygame.draw.rect(self.screen, colors.dark_brown,
                         (0, 0, self.resolution[0], self.resolution[1]/25+20))
        self.draw_health_bars(player_one_health)

    def draw_health_bars(self, player_one_health):
        upper_padding = 10
        bars_height = self.resolution[1]/25

        cur_color = self.get_health_bar_color(player_one_health)
        pygame.draw.rect(self.screen, colors.brown, (5, upper_padding,
                         self.resolution[0] * 3/7, bars_height), border_radius=255)
        pygame.draw.rect(self.screen, cur_color, (5+5, upper_padding+3,
                         (self.resolution[0] * 3/7-10) * (player_one_health/100), bars_height-6), border_radius=255)

        pygame.draw.rect(self.screen, colors.brown, (
            self.resolution[0] * 3/7 + 10, upper_padding, self.resolution[0] * 1/7-20, bars_height), border_radius=255)

        pygame.draw.rect(self.screen, colors.brown, (
            self.resolution[0] * 4/7 - 5, upper_padding, self.resolution[0] * 3/7, bars_height), border_radius=255)

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
