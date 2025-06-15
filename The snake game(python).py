import pygame
import sys
import random

#init pygame
pygame.init()

#screen size
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20

#create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('snake')

#define screen color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#define snake
snake = [[100, 100],[100, 100],[100, 100]]
direction = 'RIGHT'

#define speed
speed = 10

#define food position
food = [random.randrange(0, WIDTH, BLOCK_SIZE),random.randrange(0, HEIGHT, BLOCK_SIZE)]
clock = pygame.time.Clock()
#define score
score = 0

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_food(position):
    pygame.draw.rect(screen, RED, pygame.Rect(position[0], position[1], BLOCK_SIZE, BLOCK_SIZE))

def game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render("you lose~!", True, RED)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 25))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def game_score():
    font = pygame.font.SysFont(None, 50)
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (WIDTH // 5 - 5, HEIGHT // 2 - 300))
    pygame.display.update()

# main loop
while True:
    # keyboard
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_1:
                speed = max(1, speed - 2)
            elif event.key == pygame.K_2:
                speed = min(30, speed + 2)
            elif event.key == pygame.K_ESCAPE:
                game_over()
    # new snake head position
    head_x, head_y = snake[0]
    if direction == 'UP':
        head_y -= BLOCK_SIZE
    elif direction == 'DOWN':
        head_y += BLOCK_SIZE
    elif direction == 'LEFT':
        head_x -= BLOCK_SIZE
    elif direction == 'RIGHT':
        head_x += BLOCK_SIZE
    new_head = [head_x, head_y]

    # the wall
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        game_over()

    # itself
    if new_head in snake:
        game_over()

    # new head
    snake.insert(0, new_head)

    # eat
    if new_head == food:
        food = [random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE)]
        score = score + 10
    else:
        snake.pop()  # 没吃就删尾巴

    # update screen
    screen.fill(WHITE)
    draw_snake(snake)
    draw_food(food)
    game_score()
    pygame.display.update()

    clock.tick(speed)
