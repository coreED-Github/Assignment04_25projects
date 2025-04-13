import pygame
from pygame.locals import *
import time

pygame.font.init()

# Board data
board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

class Grid:
    def __init__(self, rows, cols, width, height, screen):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.model = [[board[i][j] for j in range(cols)] for i in range(rows)]
        self.selected = None

    def draw(self):
        gap = self.width / 9
        for i in range(self.rows + 1):
            thick = 4 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(self.screen, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)

        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] != 0:
                    text = font.render(str(board[i][j]), 1, (0, 0, 0))
                    self.screen.blit(text, (j * gap + 20, i * gap + 15))

    def select(self, row, col):
        self.selected = (row, col)

    def draw_box(self):
        if self.selected:
            gap = self.width / 9
            row, col = self.selected
            pygame.draw.rect(self.screen, (255, 0, 0), (col * gap, row * gap, gap, gap), 3)

    def place(self, val):
        row, col = self.selected
        if board[row][col] == 0:
            board[row][col] = val
            self.model[row][col] = val
            return True
        return False

    def is_full(self):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return False
        return True

    def update_model(self):
        self.model = [[board[i][j] for j in range(9)] for i in range(9)]

    def solve_gui(self):
        self.update_model()
        empty = find_empty(board)
        if not empty:
            return True
        row, col = empty

        for i in range(1, 10):
            if valid(board, i, (row, col)):
                board[row][col] = i
                self.update_model()
                self.draw()
                self.draw_box()
                pygame.display.update()
                pygame.time.delay(50)

                if self.solve_gui():
                    return True

                board[row][col] = 0
                self.update_model()
                self.draw()
                self.draw_box()
                pygame.display.update()
                pygame.time.delay(50)

        return False

def valid(bo, num, pos):
    row, col = pos
    for i in range(9):
        if bo[row][i] == num and i != col:
            return False
    for i in range(9):
        if bo[i][col] == num and i != row:
            return False
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j)
    return None

# Setup
screen = pygame.display.set_mode((540, 600))
pygame.display.set_caption("Sudoku Game")
font = pygame.font.SysFont("comicsans", 40)
grid = Grid(9, 9, 540, 540, screen)

# Main loop
running = True
key = None

while running:
    screen.fill((255, 255, 255))
    grid.draw()
    grid.draw_box()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // (540 // 9)
            col = pos[0] // (540 // 9)
            grid.select(row, col)

        if event.type == KEYDOWN:
            if event.key == K_1: key = 1
            if event.key == K_2: key = 2
            if event.key == K_3: key = 3
            if event.key == K_4: key = 4
            if event.key == K_5: key = 5
            if event.key == K_6: key = 6
            if event.key == K_7: key = 7
            if event.key == K_8: key = 8
            if event.key == K_9: key = 9

            if event.key == K_RETURN:
                grid.solve_gui()

            if event.key == K_BACKSPACE:
                row, col = grid.selected
                board[row][col] = 0

            if key is not None:
                grid.place(key)
                key = None

pygame.quit()