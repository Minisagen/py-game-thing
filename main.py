import pygame
from pygame.locals import*
pygame.display.init()
screen = pygame.display.set_mode((800, 600))
rect = pygame.Rect(400, 300, 200, 200)
color = pygame.Color(0, 100, 0, 0)
black = pygame.Color(0, 0, 0,255)
clock = pygame.time .Clock()
def move_up():
  global rect
  y =  rect.centery
  y = y + -10
  rect.centery = y
def move_down():
  global rect
  y =  rect.centery
  y = y + 10
  rect.centery = y
def move_right():
  global rect
  x =  rect.centerx
  x = x + 10
  rect.centerx = x
def move_left():
  global rect
  x =  rect.centerx
  x = x + -10
  rect.centerx = x
def main():
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit(0)
      elif event.type == KEYDOWN:
        if event.key ==K_UP:
          move_up()
        if event.key ==K_DOWN:
          move_down()
        if event.key ==K_RIGHT:
          move_right()
        if event.key ==K_LEFT:
          move_left()
    clock.tick(60)
    screen.fill(color, rect)
    
    pygame.display.flip()
    screen.fill(black)
main()