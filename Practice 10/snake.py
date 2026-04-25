import pygame
import random
import time

# Инициализация
pygame.init()

# Настройки экрана и цветов
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Шрифты
font_style = pygame.font.SysFont("bahnschrift", 25)

def show_score(score, level):
    value = font_style.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(value, [10, 10])

def generate_food(snake_list):
    """Генерация еды, чтобы она не попала на змейку"""
    while True:
        food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
        food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
        if [food_x, food_y] not in snake_list:
            return food_x, food_y

def game_loop():
    game_over = False
    
    # Начальные координаты змейки
    x, y = WIDTH / 2, HEIGHT / 2
    dx, dy = 0, 0
    
    snake_list = []
    length_of_snake = 1
    
    score = 0
    level = 1
    speed = 10  # Начальная скорость
    
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

        # 1. Проверка столкновения с границами
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        x += dx
        y += dy
        screen.fill(BLACK)
        
        # Рисуем еду
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        # Логика роста змейки
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Проверка столкновения с самим собой
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Рисуем змейку
        for segment in snake_list:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

        # 2. Проверка поедания еды
        if x == food_x and y == food_y:
            food_x, food_y = generate_food(snake_list)
            length_of_snake += 1
            score += 1
            
            # 3 & 4. Уровни и повышение скорости каждые 3 очка
            if score % 3 == 0:
                level += 1
                speed += 2 

        # 5. Отображение счета и уровня
        show_score(score, level)
        
        pygame.display.update()
        clock.tick(speed)

    pygame.quit()

game_loop()