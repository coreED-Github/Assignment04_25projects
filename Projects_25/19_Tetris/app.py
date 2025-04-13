import pygame
import random

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
ROWS = SCREEN_HEIGHT // BLOCK_SIZE
COLS = SCREEN_WIDTH // BLOCK_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

colors = [CYAN, BLUE, ORANGE, YELLOW, GREEN, MAGENTA, RED]

SHAPES = [
    [[1, 1, 1, 1]],  
    [[1, 1], [1, 1]], 
    [[0, 1, 0], [1, 1, 1]], 
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

class Tetrimino:
    def __init__(self, shape=None, color=None):
        self.shape = shape if shape else random.choice(SHAPES)
        self.color = color if color else random.choice(colors)
        self.x = int(COLS / 2) - int(len(self.shape[0]) / 2)
        self.y = 0

    def rotate(self):
        """ Rotate the tetrimino by 90 degrees """
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def create_grid():
    return [[BLACK for _ in range(COLS)] for _ in range(ROWS)]

def check_collision(grid, tetrimino):
    for y, row in enumerate(tetrimino.shape):
        for x, cell in enumerate(row):
            if cell:
                if x + tetrimino.x < 0 or x + tetrimino.x >= COLS or y + tetrimino.y >= ROWS:
                    return True
                if y + tetrimino.y >= 0 and grid[y + tetrimino.y][x + tetrimino.x] != BLACK:
                    return True
    return False

# grid
def lock_tetrimino(grid, tetrimino):
    for y, row in enumerate(tetrimino.shape):
        for x, cell in enumerate(row):
            if cell:
                grid[y + tetrimino.y][x + tetrimino.x] = tetrimino.color

#update the score
def clear_lines(grid):
    lines_cleared = 0
    for i in range(len(grid) - 1, -1, -1):
        if all(cell != BLACK for cell in grid[i]):
            grid.pop(i)
            grid.insert(0, [BLACK for _ in range(COLS)])
            lines_cleared += 1
    return lines_cleared

def draw_screen(grid, score, tetrimino):
    screen.fill(BLACK)

    for y in range(ROWS):
        for x in range(COLS):
            pygame.draw.rect(screen, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    for y, row in enumerate(tetrimino.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, tetrimino.color, ((tetrimino.x + x) * BLOCK_SIZE, (tetrimino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    font = pygame.font.SysFont('Arial', 24)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

def game():
    grid = create_grid()
    score = 0
    clock = pygame.time.Clock()
    tetrimino = Tetrimino()
    fall_time = 0
    game_over = False

    while not game_over:
        grid_copy = [row[:] for row in grid]
        tetrimino.x = int(COLS / 2) - int(len(tetrimino.shape[0]) / 2)
        tetrimino.y = 0

        while not check_collision(grid_copy, tetrimino) and not game_over:
            grid_copy = [row[:] for row in grid]
            tetrimino.y += 1
            fall_time += clock.get_rawtime()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        tetrimino.x -= 1
                        if check_collision(grid_copy, tetrimino):
                            tetrimino.x += 1
                    if event.key == pygame.K_RIGHT:
                        tetrimino.x += 1
                        if check_collision(grid_copy, tetrimino):
                            tetrimino.x -= 1
                    if event.key == pygame.K_DOWN:
                        tetrimino.y += 1
                        if check_collision(grid_copy, tetrimino):
                            tetrimino.y -= 1
                    if event.key == pygame.K_UP:
                        tetrimino.rotate()
                        if check_collision(grid_copy, tetrimino):
                            tetrimino.rotate()
                            tetrimino.rotate()
                            tetrimino.rotate()

            if check_collision(grid, tetrimino):
                tetrimino.y -= 1
                lock_tetrimino(grid, tetrimino)
                lines_cleared = clear_lines(grid)
                score += lines_cleared * 100
                tetrimino = Tetrimino()
                if check_collision(grid, tetrimino):
                    game_over = True

            draw_screen(grid, score, tetrimino)
            clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    game()