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
    buttons = interface.display_interface()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, button_rect in enumerate(buttons):
                if button_rect.collidepoint(event.pos):  # Check if mouse is over the button
                    print(f'Button {i}')
    
    p1 -= 1
    if p1 == -1:
        p1 = 100
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
