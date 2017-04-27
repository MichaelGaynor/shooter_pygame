# Duh
import pygame
# We need sys for quit
import sys

def check_events(the_player):
  for event in pygame.event.get():

    if event.type == pygame.QUIT:
    # The user clicked the red x. Get out of the loop and kill the game
      sys.exit()

    elif event.type == pygame.KEYDOWN:
      if event.key == 273:
        the_player.should_move("up", True)
      elif event.key == 274: 
        the_player.should_move("down", True)
      if event.key == 275:
        the_player.should_move("right", True)
      elif event.key == 276:
        the_player.should_move("left", True)
      # print event.key

    elif event.type == pygame.KEYUP:
      if event.key == 273:
        the_player.should_move("up", False)
      elif event.key == 274:
        the_player.should_move("down", False)
      if event.key == 275:
        the_player.should_move("right", False)
      elif event.key == 276:
        the_player.should_move("left", False)