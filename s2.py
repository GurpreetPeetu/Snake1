
import pygame
pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Game")
pygame.display.update()

# Game specific variables
exit_game = False
game_over = False

# Game Loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True



    gameWindow.fill(red)
    pygame.display.update()



pygame.quit()
quit()

