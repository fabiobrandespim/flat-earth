#!/usr/bin/env python
#https://kaleu.wordpress.com/2011/06/23/posicionamento-em-circulo-javascript/

import pygame
import math
import time
import Particle
from math import sqrt
from pygame.locals import *

img = pygame.image.load("terra_plana.bmp")

if not pygame.font:
    print 'Atencao, nao existem fontes.'

if not pygame.mixer:
    print 'Atencao, nao existe som.'


pygame.init()


vermelho = (255, 0, 0)
amarelo  = (255, 255, 0)
preto    = (0, 0, 0)
white    = (255, 64, 64)
branco   = (255, 255, 255)
azul     = (0, 0, 255)
verde    = (0, 255, 0)


pi = 3.141592653

comprimento_ecra = 820
altura_ecra      = 820
ecra             = pygame.display.set_mode((comprimento_ecra, altura_ecra))

xpos         = (comprimento_ecra)/2
ypos         = (altura_ecra)/2

raio_circulo = 15
raio         = 100


#=================================
def g2rad(graus):
   radianos = (graus * pi) / 180;
   return radianos;


#================================
def sun(raio, pontocentral,graus):
   rad = g2rad(graus);
   x = (math.cos(rad) * raio) + pontocentral;
   x = int(x)
   y = (math.sin(rad) * raio) + pontocentral;
   y = int(y)
   return (x, y)

#================================
def moon(raio, pontocentral,graus):
   rad = g2rad(graus+540);
   x = (math.cos(rad) * raio) + pontocentral;
   x = int(x)
   y = (math.sin(rad) * raio) + pontocentral;
   y = int(y)
   return (x, y)

#circulo = pygame.draw.circle(ecra, vermelho, (a, b), raio_circulo)
#circ1   = pygame.draw.circle(ecra, vermelho, (50,180), raio_circulo, 0)
#circ2   = pygame.draw.circle(ecra, vermelho, (130,180), raio_circulo, 3)


pygame.display.set_caption('Flat Earth')

pygame.display.flip()

pygame.key.set_repeat(100, 100)

graus = 0

subindo = True

cont = 1

while True:
    for event in pygame.event.get():
        pass
        #if event.type == pygame.QUIT:
        #   pygame.quit()
        #   sys.exit()

    tecla_pressionada = pygame.key.get_pressed()

    if tecla_pressionada[K_ESCAPE]:
        break

    graus += 1

    if graus > 360:
        graus = 1
        if subindo:
          if raio < 300:
             raio += 10
          else:
             subindo = False
        else:
          if raio > 100:
            raio -= 10
          else:
            subindo = True

    x1, y1 = sun(raio, 410, graus)
    x2, y2 = moon(raio, 410, graus)



    #ecra.fill(preto)
    sol = pygame.draw.circle(ecra, amarelo, (x1, y1), raio_circulo)
    lua = pygame.draw.circle(ecra, azul, (x2, y2), raio_circulo)
    pygame.display.flip()

    pygame.time.delay(1)
    #ecra.fill((white))
    ecra.blit(img,(0,0))
    #pygame.display.flip()

    pygame.draw.line(ecra, vermelho, [410, 0], [410, 820], 1)
    pygame.draw.line(ecra, vermelho, [0, 410], [820, 410], 1)
    circulo = pygame.draw.circle(ecra, amarelo, (410, 410), 100,1)
    circulo = pygame.draw.circle(ecra, amarelo, (410, 410), 200,1)
    circulo = pygame.draw.circle(ecra, amarelo, (410, 410), 300,1)

    #circulo azul no centro
    my_first_particle = Particle.Particle((410, 410), 5)
    my_first_particle.display()