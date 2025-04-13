import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
MINES_COUNT = 10
TILE_SIZE = WIDTH // COLS

BG_COLOR = (200, 200, 200)
GRID_COLOR = (100, 100, 100)
REVEALED_COLOR = (170, 170, 170)
MINE_COLOR = (255, 0, 0)
FLAG_COLOR = (255, 255, 0)

#Fonts
FONT = pygame.font.SysFont("arial", 24)

#screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

#Tile class
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.mine = False
        self.revealed = False
        self.flagged = False
        self.neighbor_mines = 0

    def draw(self):
        if self.revealed:
            pygame.draw.rect(screen, REVEALED_COLOR, self.rect)
            if self.mine:
                pygame.draw.circle(screen, MINE_COLOR, self.rect.center, TILE_SIZE // 4)
            elif self.neighbor_mines > 0:
                text = FONT.render(str(self.neighbor_mines), True, (0, 0, 0))
                screen.blit(text, (self.rect.x + TILE_SIZE // 3, self.rect.y + TILE_SIZE // 4))
        else:
            pygame.draw.rect(screen, BG_COLOR, self.rect)
            if self.flagged:
                pygame.draw.circle(screen, FLAG_COLOR, self.rect.center, TILE_SIZE // 4)
        pygame.draw.rect(screen, GRID_COLOR, self.rect, 1)

#Create grid
grid = [[Tile(x, y) for y in range(ROWS)] for x in range(COLS)]

def get_neighbors(tile):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = tile.x + dx, tile.y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS:
                neighbors.append(grid[nx][ny])
    return neighbors

def place_mines():
    mines_placed = 0
    while mines_placed < MINES_COUNT:
        x = random.randint(0, COLS - 1)
        y = random.randint(0, ROWS - 1)
        tile = grid[x][y]
        if not tile.mine:
            tile.mine = True
            for neighbor in get_neighbors(tile):
                neighbor.neighbor_mines += 1
            mines_placed += 1

def reveal(tile):
    if tile.revealed or tile.flagged:
        return
    tile.revealed = True
    if tile.mine:
        game_over()
    elif tile.neighbor_mines == 0:
        for neighbor in get_neighbors(tile):
            reveal(neighbor)

def game_over():
    for row in grid:
        for tile in row:
            tile.revealed = True

def check_win():
    for row in grid:
        for tile in row:
            if not tile.mine and not tile.revealed:
                return False
    return True

place_mines()

# Game loop
running = True
while running:
    screen.fill(BG_COLOR)
    for row in grid:
        for tile in row:
            tile.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            tile = grid[x // TILE_SIZE][y // TILE_SIZE]
            if event.button == 1:
                reveal(tile)
                if check_win():
                    print("You win!")
                    running = False
            elif event.button == 3:
                if not tile.revealed:
                    tile.flagged = not tile.flagged

pygame.quit()
sys.exit()