# Duh
import pygame
# We need sys for quit
import sys

def check_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
    # The user clicked the red x. Get out of the loop and kill the game
      sys.exit()