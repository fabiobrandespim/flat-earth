import pygame
from pygame.locals import *

img = pygame.image.load("terra_plana.bmp")

white = (255, 64, 64)
w = 820
h = 820
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = 1

while running:
  #screen.fill((white))
  screen.blit(img,(0,0))
  pygame.display.flip()