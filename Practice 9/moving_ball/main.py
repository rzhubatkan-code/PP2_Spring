import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

my_ball = Ball(WIDTH // 2, HEIGHT // 2, 25, RED, WIDTH, HEIGHT)

clock = pygame.time.Clock()
running=True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my_ball.move("UP")
            elif event.key == pygame.K_DOWN:
                my_ball.move("DOWN")
            elif event.key == pygame.K_LEFT:
                my_ball.move("LEFT")
            elif event.key == pygame.K_RIGHT:
                my_ball.move("RIGHT")

    my_ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
