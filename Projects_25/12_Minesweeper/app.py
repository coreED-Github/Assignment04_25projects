import pygame
import pygame_menu
import random
import sys

pygame.init()

TILE_SIZE = 40
WINDOW_HEIGHT_EXTRA = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (160, 160, 160)
RED = (255, 0, 0)

GRID_SIZE = 10
MINE_COUNT = 10
WINDOW_WIDTH = GRID_SIZE * TILE_SIZE
WINDOW_HEIGHT = GRID_SIZE * TILE_SIZE + WINDOW_HEIGHT_EXTRA

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Minesweeper")
font = pygame.font.SysFont('arial', 20)


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_mine = False
        self.revealed = False
        self.flagged = False
        self.neighbor_mines = 0

    def draw(self, surface):
        rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        if self.revealed:
            pygame.draw.rect(surface, WHITE, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)
            if self.has_mine:
                pygame.draw.circle(surface, BLACK, rect.center, TILE_SIZE // 4)
            elif self.neighbor_mines > 0:
                text = font.render(str(self.neighbor_mines), True, BLACK)
                surface.blit(text, text.get_rect(center=rect.center))
        else:
            pygame.draw.rect(surface, GRAY, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)
            if self.flagged:
                pygame.draw.circle(surface, RED, rect.center, TILE_SIZE // 4)


class MinesweeperGame:
    def __init__(self, window, grid_size, mine_count):
        self.window = window
        self.grid_size = grid_size
        self.mine_count = mine_count
        self.grid = []
        self.game_over = False
        self.first_click = True
        self.flags_left = mine_count
        self.gameover_menu = None
        self.create_grid()
        self.create_gameover_menu()

    def create_grid(self):
        self.grid = [[Tile(x, y) for y in range(self.grid_size)] for x in range(self.grid_size)]

    def reset(self):
        self.__init__(self.window, self.grid_size, self.mine_count)

    def create_gameover_menu(self):
        self.gameover_menu = pygame_menu.Menu('Game Over', WINDOW_WIDTH, WINDOW_HEIGHT, theme=pygame_menu.themes.THEME_DARK)
        self.gameover_menu.add.label('You hit a mine!')
        self.gameover_menu.add.button('Play Again', self.reset)
        self.gameover_menu.add.button('Main Menu', lambda: start_menu.mainloop(window))
        self.gameover_menu.add.button('Quit', pygame_menu.events.EXIT)

    def place_mines(self, safe_x, safe_y):
        mines_placed = 0
        while mines_placed < self.mine_count:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if not self.grid[x][y].has_mine and (x != safe_x or y != safe_y):
                self.grid[x][y].has_mine = True
                mines_placed += 1

        for x in range(self.grid_size):
            for y in range(self.grid_size):
                self.grid[x][y].neighbor_mines = self.count_neighbor_mines(x, y)

    def count_neighbor_mines(self, x, y):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                    if self.grid[nx][ny].has_mine:
                        count += 1
        return count

    def reveal_tile(self, x, y):
        tile = self.grid[x][y]
        if tile.revealed or tile.flagged:
            return
        tile.revealed = True
        if tile.has_mine:
            self.game_over = True
            self.display_gameover_menu()
        elif tile.neighbor_mines == 0:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                        self.reveal_tile(nx, ny)

    def left_click(self, pos):
        if self.game_over:
            return
        x, y = pos[0] // TILE_SIZE, pos[1] // TILE_SIZE
        if x >= self.grid_size or y >= self.grid_size:
            return
        if self.first_click:
            self.place_mines(x, y)
            self.first_click = False
        self.reveal_tile(x, y)

    def right_click(self, pos):
        if self.game_over:
            return
        x, y = pos[0] // TILE_SIZE, pos[1] // TILE_SIZE
        if x >= self.grid_size or y >= self.grid_size:
            return
        tile = self.grid[x][y]
        if not tile.revealed:
            tile.flagged = not tile.flagged

    def draw(self):
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                self.grid[x][y].draw(self.window)
        flag_text = font.render(f"Flags left: {self.flags_left}", True, BLACK)
        self.window.blit(flag_text, (10, self.grid_size * TILE_SIZE + 10))

    def display_gameover_menu(self):
        self.gameover_menu.mainloop(self.window)


def start_game(difficulty):
    global GRID_SIZE, MINE_COUNT, WINDOW_WIDTH, WINDOW_HEIGHT, window
    if difficulty == 'Easy':
        GRID_SIZE = 8
        MINE_COUNT = 10
    elif difficulty == 'Medium':
        GRID_SIZE = 10
        MINE_COUNT = 15
    elif difficulty == 'Hard':
        GRID_SIZE = 12
        MINE_COUNT = 25

    WINDOW_WIDTH = GRID_SIZE * TILE_SIZE
    WINDOW_HEIGHT = GRID_SIZE * TILE_SIZE + WINDOW_HEIGHT_EXTRA
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    game = MinesweeperGame(window, GRID_SIZE, MINE_COUNT)
    run_game(game)


def run_game(game):
    clock = pygame.time.Clock()
    running = True

    while running:
        window.fill(WHITE)
        game.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    game.left_click(event.pos)
                elif event.button == 3:
                    game.right_click(event.pos)

        clock.tick(30)

    pygame.quit()
    sys.exit()

start_menu = pygame_menu.Menu('Minesweeper', 400, 300, theme=pygame_menu.themes.THEME_SOLARIZED)
start_menu.add.label('Select Difficulty:')
start_menu.add.button('Easy', lambda: start_game('Easy'))
start_menu.add.button('Medium', lambda: start_game('Medium'))
start_menu.add.button('Hard', lambda: start_game('Hard'))
start_menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    start_menu.mainloop(window)
