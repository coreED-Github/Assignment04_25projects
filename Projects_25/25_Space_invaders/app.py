import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

player_img = pygame.image.load('assets/player.png')
player_img = pygame.transform.scale(player_img, (64, 64))

enemy_img = pygame.image.load('assets/enemy.png')
enemy_img = pygame.transform.scale(enemy_img, (64, 64))

bullet_img = pygame.Surface((4, 20))
bullet_img.fill((255, 255, 0))

icon = pygame.image.load('assets/space_icon.png')
pygame.display.set_icon(icon)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(20, 150)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed = random.randint(1, 3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

player = Player()
player_group = pygame.sprite.Group(player)

bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
for _ in range(6):
    enemies.add(Enemy())

clock = pygame.time.Clock()
running = True
score = 0
font = pygame.font.SysFont(None, 36)

while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.add(Bullet(player.rect.centerx, player.rect.top))

    # Update
    keys = pygame.key.get_pressed()
    player.update(keys)
    bullets.update()
    enemies.update()

    # Collision
    for bullet in bullets:
        hits = pygame.sprite.spritecollide(bullet, enemies, True)
        for enemy in hits:
            bullet.kill()
            score += 1
            enemies.add(Enemy())

    # Draw
    player_group.draw(screen)
    bullets.draw(screen)
    enemies.draw(screen)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
