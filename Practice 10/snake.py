import pygame
import random
import time


pygame.init()


WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0) 


font_style = pygame.font.SysFont("bahnschrift", 25)
big_font = pygame.font.SysFont("bahnschrift", 50)

def show_score(score, level):
    value = font_style.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(value, [10, 10])

def generate_food(snake_list):
    while True:
        food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
        food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
        if [food_x, food_y] not in snake_list:
            return food_x, food_y

def game_loop():
    game_over = False
    
    x, y = WIDTH / 2, HEIGHT / 2
    dx, dy = 0, 0
    
    snake_list = []
    length_of_snake = 1
    
    score = 0
    level = 1
    speed = 10 
    
    food_x, food_y = generate_food(snake_list)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK_SIZE

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        x += dx
        y += dy
        screen.fill(BLACK)
        
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        for segment in snake_list:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        
        if x == food_x and y == food_y:
            food_x, food_y = generate_food(snake_list)
            length_of_snake += 1
            score += 1
            
           
            if score > 0 and score % 3 == 0:
                level += 1
                speed += 3 
                
               
                msg = big_font.render("LEVEL UP!", True, YELLOW)
                screen.blit(msg, [WIDTH / 3, HEIGHT / 3])
                pygame.display.update()
                time.sleep(0.3) 

        show_score(score, level)
        
        pygame.display.update()
        clock.tick(speed)

    pygame.quit()

game_loop()