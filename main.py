import pygame
from pygame.locals import *

pygame.init()

def draw():
    gui.fill((0, 0, 0))
    gui.blit(astro, (astro_x, astro_y))
    pygame.display.flip()

pygame.display.set_caption("Astronaut in the ocean :)")
gui = pygame.display.set_mode((800, 800))
astro_x = 50
astro_y = 50
astro = pygame.image.load("./pixil-frame-0.png").convert()

gui.fill((0, 0, 0))
gui.blit(astro, (200, 250))
pygame.display.flip()

running = True

while running == True:
    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_UP:
                astro_y -= 10
                draw()

            if event.key == K_DOWN:
                astro_y += 10
                draw()

            if event.key == K_LEFT:
                astro_x -= 10
                draw()

            if event.key == K_RIGHT:
                astro_x += 10
                draw()

        elif event.type == QUIT:
            running == False
