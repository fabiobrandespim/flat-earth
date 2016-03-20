import pygame

comprimento_ecra = 820
altura_ecra      = 820
ecra             = pygame.display.set_mode((comprimento_ecra, altura_ecra))

class titulo:
   def __init__(self, nome, linha):
     self.nome = nome
     self.linha = linha


   def display(self):
     font            = pygame.font.Font(None, 25)
     text            = font.render(self.nome, 1, (255,255,255))
     textpos         = text.get_rect()
     textpos.centerx = ecra.get_rect().centerx
     textpos.centery = self.linha
     ecra.blit(text, textpos)