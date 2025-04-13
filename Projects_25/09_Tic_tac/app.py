import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 20
SPACE = SQUARE_SIZE // 4

#Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

#Fonts
FONT = pygame.font.SysFont("comicsans", 40)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

#Board
board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

player = 1
game_over = False
vs_computer = False

#Draw lines
def draw_lines():
    screen.fill(BG_COLOR)
    for i in range(1, BOARD_ROWS):
        # Horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        # Vertical
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                # Draw X
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                start_asc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)
            elif board[row][col] == 2:
                # Draw O
                center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def is_available(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in board:
        if 0 in row:
            return False
    return True

def check_win(player):

    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):
            draw_win_line((i, 0), (i, 2))
            return True
        if all([board[j][i] == player for j in range(3)]):
            draw_win_line((0, i), (2, i))
            return True

    # Diagonals
    if all([board[i][i] == player for i in range(3)]):
        draw_win_line((0, 0), (2, 2))
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        draw_win_line((0, 2), (2, 0))
        return True
    return False

def draw_win_line(start, end):
    x1 = start[1] * SQUARE_SIZE + SQUARE_SIZE // 2
    y1 = start[0] * SQUARE_SIZE + SQUARE_SIZE // 2
    x2 = end[1] * SQUARE_SIZE + SQUARE_SIZE // 2
    y2 = end[0] * SQUARE_SIZE + SQUARE_SIZE // 2
    pygame.draw.line(screen, (255, 0, 0), (x1, y1), (x2, y2), 10)

def restart():
    global board, player, game_over
    board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 1
    game_over = False
    draw_lines()

def computer_move():
    available = [(r, c) for r in range(3) for c in range(3) if board[r][c] == 0]
    if available:
        move = random.choice(available)
        mark_square(move[0], move[1], 2)
        if check_win(2):
            # win_sound.play()
            return True
    return False

draw_lines()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # click_sound.play()
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE

                if is_available(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = 2 if player == 1 else 1

                    if vs_computer and player == 2 and not game_over:
                        pygame.time.delay(500)
                        if computer_move():
                            game_over = True
                        player = 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()

    draw_figures()
    pygame.display.update()