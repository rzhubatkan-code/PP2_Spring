#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
COIN_SPEED = 5
N = 10

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.weight = random.choice([1, 2, 3, 5])

        size = 20 + (self.weight *5)
        original_image = pygame.image.load("coin2.png")
        self.image = pygame.transform.scale(original_image, (size, size))

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > 600:
            self.reset()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
coins.add(C1)
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.init()
pygame.mixer.music.load("background.wav")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Отрисовка фона и счета
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render("Enemies: " + str(SCORE), True, BLACK)
    coin_text = font_small.render("Coins: " + str(COIN_SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_text, (280, 10))

    # Движение всех объектов
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # ПРОВЕРКА: Сбор монеты
    if pygame.sprite.spritecollide(P1, coins, False):
        # Получаем объект монеты, с которой столкнулись
        for coin in coins:
            COIN_SCORE += coin.weight  # Прибавляем вес монеты к счету
            
            # 2. УСКОРЕНИЕ: Если набрали N монет, увеличиваем скорость врага
            if COIN_SCORE % N == 0:
                SPEED += 1
            
            coin.reset() # Спавним новую монету

    # ПРОВЕРКА: Столкновение с врагом
    if pygame.sprite.spritecollideany(P1, enemies):
        # Останавливаем всё и играем звуки
        pygame.mixer.music.stop()
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        
        try:
            # Пытаемся включить музыку проигрыша
            pygame.mixer.music.load("game_over.mp3")
            pygame.mixer.music.play()
        except:
            pass # Если файла нет, просто идем дальше

        # Отображаем картинку проигрыша
        try:
            game_over_bg = pygame.image.load("game_over_bg.png")
            game_over_bg = pygame.transform.scale(game_over_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
            DISPLAYSURF.blit(game_over_bg, (0,0))
        except:
            DISPLAYSURF.fill(RED) # Если картинки нет, будет красный экран
            
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        
        time.sleep(4)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
