

import pygame
pygame.init()

# Creating window
gameWindow = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Sapp Wali game")

# Game specific variables
exit_game = False
game_over = False

# Creating a game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)

pygame.quit()
quit()

