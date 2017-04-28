import pygame #Duh
from pygame.sprite import Sprite

class Bullet(Sprite):
  def __init__(self, screen, hero, direction):
    super(Bullet, self).__init__()
    self.screen = screen
    self.rect = pygame.Rect((0,0),(20,5)) #Make a bullet
    self.rect.centerx = hero.rect.centerx
    self.rect.top = hero.rect.top
    self.color = (255,0,255)
    self.speed = 10
    self.y = self.rect.y
    self.x = self.rect.x
    self.direction = direction

  def update(self):
    # if self.direction == 1: #up
    #   self.y -= self.speed #change the y, each time update is run, by bullet speed
    #   self.rect.y = self.y #update rect position
    if self.direction == 1: #right
      self.x += self.speed #change the y, each time update is run, by bullet speed
      self.rect.x = self.x #update rect position
    # elif self.direction == 3: #down
    #   self.y += self.speed #change the y, each time update is run, by bullet speed
    #   self.rect.y = self.y #update rect position
    # elif self.direction == 2: #left
    #   self.x -= self.speed #change the y, each time update is run, by bullet speed
    #   self.rect.x = self.x #update rect position


  def draw_bullet(self):
    pygame.draw.rect(self.screen, self.color, self.rect) #draw the bullet!

