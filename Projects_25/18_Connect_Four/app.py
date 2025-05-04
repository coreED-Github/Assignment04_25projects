import pygame
import sys
import numpy as np
import math
import random

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 80
RADIUS = int(SQUARESIZE / 2 - 8)
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 2) * SQUARESIZE
size = (width, height)

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect Four")
clock = pygame.time.Clock()

myfont = pygame.font.SysFont("monospace", 50)
small_font = pygame.font.SysFont("arial", 28)

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if all(board[r][c+i] == piece for i in range(4)):
                return [(r, c+i) for i in range(4)]

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return [(r+i, c) for i in range(4)]

    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return [(r-i, c+i) for i in range(4)]

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return [(r+i, c+i) for i in range(4)]
    return None

def square_win(board, piece):
    for c in range(COLUMN_COUNT - 1):
        for r in range(ROW_COUNT - 1):
            if board[r][c] == board[r+1][c] == board[r][c+1] == board[r+1][c+1] == piece:
                return [(r, c), (r+1, c), (r, c+1), (r+1, c+1)]
    return None

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, (r+1)*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int((r+1)*SQUARESIZE + SQUARESIZE/2)), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            piece = board[r][c]
            if piece == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE + SQUARESIZE/2), int((r+1)*SQUARESIZE + SQUARESIZE/2)), RADIUS)
            elif piece == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE + SQUARESIZE/2), int((r+1)*SQUARESIZE + SQUARESIZE/2)), RADIUS)

def highlight_winning_line(line):
    for r, c in line:
        pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE + SQUARESIZE/2), int((r+1)*SQUARESIZE + SQUARESIZE/2)), RADIUS + 5)

def draw_message(text, color):
    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
    label = myfont.render(text, True, color)
    screen.blit(label, (40, 10))
    pygame.display.update()

def computer_move(board):
    valid_cols = [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]
    return random.choice(valid_cols)

def draw_endgame_options():
    pygame.draw.rect(screen, GREY, (width//2 - 140, height - 70, 120, 50))
    pygame.draw.rect(screen, GREY, (width//2 + 20, height - 70, 120, 50))
    screen.blit(small_font.render("Quit", True, BLACK), (width//2 - 110, height - 60))
    screen.blit(small_font.render("Continue", True, BLACK), (width//2 + 30, height - 60))
    pygame.display.update()

def animate_fill_bottom_to_top(board, col, row, piece):
    for r in range(ROW_COUNT - 1, row - 1, -1):
        board[r][col] = piece
        draw_board(board)
        pygame.display.update()
        pygame.time.wait(50)
        if r != row:
            board[r][col] = 0

board = create_board()
turn = 0
game_over = False

draw_board(board)
draw_message("Your Turn", RED)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if width//2 - 140 <= x <= width//2 - 20 and height - 70 <= y <= height - 20:
                    pygame.quit()
                    sys.exit()
                elif width//2 + 20 <= x <= width//2 + 140 and height - 70 <= y <= height - 20:
                    board = create_board()
                    draw_board(board)
                    turn = 0
                    game_over = False
                    draw_message("Your Turn", RED)

        elif turn == 0 and event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            col = int(math.floor(event.pos[0] / SQUARESIZE))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                animate_fill_bottom_to_top(board, col, row, 1)
                drop_piece(board, row, col, 1)
                win_line = winning_move(board, 1) or square_win(board, 1)
                draw_board(board)

                if win_line:
                    highlight_winning_line(win_line)
                    draw_message("You Win!", GREEN)
                    game_over = True
                    draw_endgame_options()
                else:
                    turn = 1
                    draw_message("Computer Turn", YELLOW)

    if not game_over and turn == 1:
        pygame.time.wait(600)
        col = computer_move(board)
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            animate_fill_bottom_to_top(board, col, row, 2)
            drop_piece(board, row, col, 2)
            win_line = winning_move(board, 2) or square_win(board, 2)
            draw_board(board)

            if win_line:
                highlight_winning_line(win_line)
                draw_message("You Lost!", RED)
                game_over = True
                draw_endgame_options()
            else:
                turn = 0
                draw_message("Your Turn", RED)

    pygame.display.update()
    clock.tick(60)

