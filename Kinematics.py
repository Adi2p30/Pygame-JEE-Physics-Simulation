import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, speed):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(speed * math.cos(math.radians(angle)),
                                       speed * math.sin(math.radians(angle)))
        self.gravity = pygame.math.Vector2(0, 0.5)

    def update(self):
        self.vel += self.gravity
        self.pos += self.vel
        self.rect.center = self.pos

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Motion Simulation")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# Create projectile
projectile = Projectile(WIDTH // 2, HEIGHT - 30, 45, 10)
all_sprites.add(projectile)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
