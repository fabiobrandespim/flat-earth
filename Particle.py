import pygame


comprimento_ecra = 820
altura_ecra      = 820
ecra             = pygame.display.set_mode((comprimento_ecra, altura_ecra))


class Particle:
   def __init__(self, (x, y), size):
     self.x = x
     self.y = y
     self.size = size
     self.colour = (255, 255, 255)
     self.thickness = 1


   def display(self):
     pygame.draw.circle(ecra, self.colour, (self.x, self.y), self.size, self.thickness)