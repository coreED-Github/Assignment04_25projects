import pygame
import random
import sys

pygame.init()

#settings
WIDTH, HEIGHT = 900, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Runner - Ultimate Edition")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)
# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)

GRAVITY = 1
LEVEL_TIME = 45

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = HEIGHT - 100
        self.vel_y = 0
        self.health = 5
        self.score = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 6
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 6
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= 6
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += 6

class Treasure(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((25, 25))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=(x, y))

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed *= -1

def draw_text(text, size, x, y, color=WHITE):
    font_obj = pygame.font.SysFont("Arial", size, bold=True)
    text_surf = font_obj.render(text, True, color)
    SCREEN.blit(text_surf, (x, y))

def draw_health_bar(health):
    pygame.draw.rect(SCREEN, RED, (20, 20, 120, 25))
    pygame.draw.rect(SCREEN, GREEN, (20, 20, 24 * health, 25))
    draw_text("Health", 22, 20, 50)

def draw_timer(seconds_left):
    draw_text(f"Time: {int(seconds_left)}s", 22, WIDTH - 150, 20)

#function
def run_game(level):
    player = Player()
    player_group = pygame.sprite.Group(player)
    treasure_group = pygame.sprite.Group()
    obstacle_group = pygame.sprite.Group()

    for _ in range(5 + level * 2):
        x = random.randint(200, WIDTH - 50)
        y = random.randint(100, HEIGHT - 100)
        treasure_group.add(Treasure(x, y))

    for _ in range(3 + level):
        x = random.randint(100, WIDTH - 100)
        y = random.randint(150, HEIGHT - 100)
        speed = random.choice([-3 - level, 3 + level])
        obstacle_group.add(Obstacle(x, y, speed))

    start_ticks = pygame.time.get_ticks()

    running = True
    while running:
        clock.tick(60)
        SCREEN.fill((30, 30, 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        seconds_passed = (pygame.time.get_ticks() - start_ticks) / 1000
        time_left = max(0, LEVEL_TIME - seconds_passed)

        player_group.update()
        obstacle_group.update()

        player_group.draw(SCREEN)
        treasure_group.draw(SCREEN)
        obstacle_group.draw(SCREEN)

        draw_health_bar(player.health)
        draw_timer(time_left)
        draw_text(f"Score: {player.score}", 22, WIDTH // 2 - 50, 20)

        #Collision
        hits = pygame.sprite.spritecollide(player, treasure_group, True)
        if hits:
            player.score += len(hits)

        if pygame.sprite.spritecollide(player, obstacle_group, False):
            player.health -= 1
            pygame.time.delay(300)
            if player.health <= 0:
                return "gameover"

        if player.score >= len(treasure_group) + len(hits):
            return "win"

        if time_left <= 0:
            return "timeout"

        pygame.display.flip()

#Screens
def end_screen(result):
    SCREEN.fill(BLACK)
    if result == "win":
        draw_text("LEVEL COMPLETE!", 50, WIDTH // 2 - 180, HEIGHT // 2 - 50, GREEN)
    elif result == "timeout":
        draw_text("TIME UP!", 50, WIDTH // 2 - 100, HEIGHT // 2 - 50, YELLOW)
    else:
        draw_text("GAME OVER!", 50, WIDTH // 2 - 150, HEIGHT // 2 - 50, RED)
    draw_text("Press R to Restart | Q to Quit", 28, WIDTH // 2 - 180, HEIGHT // 2 + 10, WHITE)
    pygame.display.flip()
    wait_for_input()

def wait_for_input():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main():
    level = 1
    while level <= 3:
        result = run_game(level)
        if result == "win":
            level += 1
        else:
            end_screen(result)
            return
    SCREEN.fill(BLUE)
    draw_text("CONGRATULATIONS! You completed all levels!", 32, WIDTH // 2 - 300, HEIGHT // 2 - 20, YELLOW)
    draw_text("Press Q to Quit", 28, WIDTH // 2 - 100, HEIGHT // 2 + 40, WHITE)
    pygame.display.flip()
    wait_for_input()

if __name__ == "__main__":
    main()