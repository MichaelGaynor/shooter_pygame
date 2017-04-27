# Duh
import pygame
# We need sys for quit
import sys
from bullet import Bullet

def check_events(the_player,screen,bullets):
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
      if event.key == 32:
        for direction in range(1,5):
          new_bullet = Bullet(screen,the_player,direction)
          bullets.add(new_bullet)
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