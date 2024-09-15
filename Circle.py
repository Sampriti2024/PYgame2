import pygame
pygame.init()

screen_width = 500
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("My First Game")
Blue = (0,0,255)
pygame.draw.circle(screen,Blue,(300,300),50)
pygame.draw.circle(screen,Blue,(100,100),50,3)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
    