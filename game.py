# THE REASON YOU HAVE ACCESS TO THIS MODULE IS BECAUSE YOU RAN:
# -----$ PIP INSTALL PYGAME
# PYGAME IS NOT PART OF CORE LIKE MATH OR RANDOM ARE
import pygame

# Import the player class from player
from random import randint
from player import Player
from game_functions import check_events

# THE CORE GAME FUNCTIONALITY/LOOP
def run_game():
# INITIALIZE ALL THE PYGAME STUFF
  pygame.init()
  # Set up a tuple for the screen size: (horizontal, vertical)
  screen_size = (1000,800)
  # Set up a tuple for the bg color
  background_color = (140,200,150)

  # Create a pygame screen to use
  screen = pygame.display.set_mode(screen_size)
  # Set a caption on the terminal window
  pygame.display.set_caption("A heroic 3rd person shooter")

  the_player = Player(screen)

  r = 0
  b = 0
  g = 0

  # Main game loop run forever or until break
  while 1:
    # if r >=
    # r += 10
    # b += 10
    # g += 10
    # background_color = (r,b,g)
    screen.fill(background_color)
    # The escape hatch from while

    check_events()

    # Draw the player
    the_player.draw_me()

        # Clear the screen for the next time through the loop
    pygame.display.flip()

# Start the game!
run_game()