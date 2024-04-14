# Package Import
import pygame
import sys

from classes.tank_class import tankClass

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('RPG Game')
clock = pygame.time.Clock()

tank = pygame.image.load('assets/tank.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        screen.blit(tank, (200,100))
        pygame.display.update()
        clock.tick(60)
