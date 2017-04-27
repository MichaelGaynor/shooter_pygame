# THE REASON YOU HAVE ACCESS TO THIS MODULE IS BECAUSE YOU RAN:
# -----$ PIP INSTALL PYGAME
# PYGAME IS NOT PART OF CORE LIKE MATH OR RANDOM ARE
import pygame

# Import the player class from player
from random import randint
from player import Player
from enemy import Enemy
from game_functions import check_events
from pygame.sprite import Group, groupcollide

# THE CORE GAME FUNCTIONALITY/LOOP
def run_game():
# INITIALIZE ALL THE PYGAME STUFF
  pygame.init()
  # Set up a tuple for the screen size: (horizontal, vertical)
  screen_size = (1000,800)
  # Set up a tuple for the bg color
  # background_color = (140,200,150)
  background_color = (255,245,255)

  # Create a pygame screen to use
  screen = pygame.display.set_mode(screen_size)
  # Set a caption on the terminal window
  pygame.display.set_caption("A the_player.ic 3rd person shooter")

  the_player = Player(screen,"./images 2/Hero.png",200,200)
  the_enemy = Enemy(screen)
  # a_bullet = Bullet(screen,the_player,)
  the_player_group = Group()
  the_player_group.add(the_player)
  enemies = Group()
  enemies.add(the_enemy)
  bullets = Group()

  tick = 0

  # Main game loop run forever or until break
  while 1:
    tick += 1
    if tick % 300 == 0:
      enemies.add(Enemy(screen))
    screen.fill(background_color)
    # The escape hatch from while

    check_events(the_player,screen,bullets)

    # Draw the player
    for player in the_player_group:
      the_player.draw_me()
    
    the_enemy.update_me(the_player)
    
    for enemy in enemies:
      the_enemy.draw_me()

    for bullet in bullets:
      bullet.update()
      bullet.draw_bullet()

    player_died = groupcollide(the_player_group, enemies, True, False)
    enemy_died = groupcollide(enemies, bullets, True, True)
        # Clear the screen for the next time through the loop
    pygame.display.flip()

# Start the game!
run_game()