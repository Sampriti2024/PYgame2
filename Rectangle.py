import pygame
pygame.init()

screen_width = 500
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My First Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen,(0,125,255),pygame.Rect(30,30,50,50))
    pygame.display.flip()