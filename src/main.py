import pygame
from interface import Interface
from game import Game

pygame.init()
game = Game("gracz 1", "gracz 2")
clock = pygame.time.Clock()
running = True
interface = Interface(game)
p1 = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    interface.display_interface()
    p1 -= 1
    if p1 == -1:
        p1 = 100
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
