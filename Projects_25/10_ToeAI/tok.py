import pygame
import sys
import math

pygame.init()
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE//4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI')
screen.fill(BG_COLOR)

# Board setup
board = [["" for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

def draw_lines():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                start = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start, end, CROSS_WIDTH)
                start = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start, end, CROSS_WIDTH)
            elif board[row][col] == 'O':
                center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_moves():
    return [(r, c) for r in range(BOARD_ROWS) for c in range(BOARD_COLS) if board[r][c] == ""]

def is_winner(player):
    for row in range(BOARD_ROWS):
        if all(board[row][col] == player for col in range(BOARD_COLS)):
            return True
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            return True
    if all(board[i][i] == player for i in range(BOARD_COLS)):
        return True
    if all(board[i][BOARD_COLS - i - 1] == player for i in range(BOARD_COLS)):
        return True
    return False

def is_board_full():
    return all(board[row][col] != "" for row in range(BOARD_ROWS) for col in range(BOARD_COLS))

def minimax(is_maximizing):
    if is_winner("O"):
        return {"score": 1}
    elif is_winner("X"):
        return {"score": -1}
    elif is_board_full():
        return {"score": 0}

    if is_maximizing:
        best = {"score": -math.inf}
        for (r, c) in available_moves():
            board[r][c] = "O"
            score = minimax(False)
            board[r][c] = ""
            score["move"] = (r, c)
            if score["score"] > best["score"]:
                best = score
        return best
    else:
        best = {"score": math.inf}
        for (r, c) in available_moves():
            board[r][c] = "X"
            score = minimax(True)
            board[r][c] = ""
            score["move"] = (r, c)
            if score["score"] < best["score"]:
                best = score
        return best

def restart():
    global board
    board = [["" for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    screen.fill(BG_COLOR)
    draw_lines()

draw_lines()
game_over = False
player_turn = True 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] == "":
                mark_square(clicked_row, clicked_col, "X")
                draw_figures()
                if is_winner("X"):
                    print("You win!")
                    game_over = True
                elif is_board_full():
                    print("It's a draw!")
                    game_over = True
                else:
                    # AI turn
                    ai_move = minimax(True)["move"]
                    mark_square(ai_move[0], ai_move[1], "O")
                    draw_figures()
                    if is_winner("O"):
                        print("Computer wins!")
                        game_over = True
                    elif is_board_full():
                        print("It's a draw!")
                        game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player_turn = True

    pygame.display.update()