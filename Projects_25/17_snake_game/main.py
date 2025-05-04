import pygame
import random
import sys

WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS = 6

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 155, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = (BLOCK_SIZE, 0)

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, new_direction):
        if (new_direction[0] != -self.direction[0] and new_direction[1] != -self.direction[1]):
            self.direction = new_direction

    def check_collision(self, walls=[]):
        head = self.body[0]
        if head in self.body[1:] or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            return True
        for wall in walls:
            if head == wall:
                return True
        return False

class Food:
    def __init__(self, snake, walls=[]):
        while True:
            x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            if (x, y) not in snake.body and (x, y) not in walls:
                self.position = (x, y)
                break

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, BLOCK_SIZE, BLOCK_SIZE))

def draw_snake(snake):
    for block in snake.body:
        pygame.draw.rect(screen, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, DARK_GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, BLUE, (*wall, BLOCK_SIZE, BLOCK_SIZE))

def draw_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

def game_over_screen(score, mode, target):
    screen.fill(BLACK)
    msg = font.render(f"Game Over! Score: {score}", True, RED)
    screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 30))
    if mode == "EASY":
        goal_text = font.render(f"Target was: {target}", True, WHITE)
        screen.blit(goal_text, (WIDTH // 2 - goal_text.get_width() // 2, HEIGHT // 2))

    quit_text = font.render("Quit (Q)", True, WHITE)
    continue_text = font.render("Continue (C)", True, WHITE)
    screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 40))
    screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT // 2 + 80))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_c:
                    game_loop()  # Restart the game loop after a loss
                    return

def difficulty_screen():
    while True:
        screen.fill(BLACK)
        title = font.render("Select Difficulty", True, WHITE)
        easy_text = font.render("1. EASY (Target Score)", True, GREEN)
        hard_text = font.render("2. HARD (With Walls)", True, BLUE)

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        screen.blit(easy_text, (WIDTH // 2 - easy_text.get_width() // 2, 160))
        screen.blit(hard_text, (WIDTH // 2 - hard_text.get_width() // 2, 200))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "EASY"
                elif event.key == pygame.K_2:
                    return "HARD"

def generate_internal_walls():
    walls = []
    for x in range(100, 500, 100):
        for y in range(100, 300, 100):
            walls.append((x, y))
    return walls

def game_loop():
    mode = difficulty_screen()
    snake = Snake()
    walls = generate_internal_walls() if mode == "HARD" else []
    target = random.randint(5, 15) if mode == "EASY" else None
    food = Food(snake, walls)
    score = 0

    running = True
    while running:
        screen.fill(BLACK)
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -BLOCK_SIZE))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, BLOCK_SIZE))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-BLOCK_SIZE, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((BLOCK_SIZE, 0))

        snake.move()

        if snake.check_collision(walls):
            game_over_screen(score, mode, target)
            return

        if snake.body[0] == food.position:
            snake.grow()
            score += 1
            if mode == "EASY" and score >= target:
                game_over_screen(score, mode, target)
                return
            food = Food(snake, walls)

        draw_snake(snake)
        food.draw()
        draw_score(score)
        if mode == "HARD":
            draw_walls(walls)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    game_loop()
