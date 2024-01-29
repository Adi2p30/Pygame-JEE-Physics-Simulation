import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CANNON_COLOR = (0, 128, 255)
PROJECTILE_COLOR = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Motion Game")

# Create the cannon
cannon_width, cannon_height = 50, 20
cannon_x, cannon_y = (WIDTH - cannon_width) // 2, HEIGHT - cannon_height
cannon = pygame.Rect(cannon_x, cannon_y, cannon_width, cannon_height)

# Cannon angle and initial projectile velocity
cannon_angle = 45  # initial angle in degrees
projectile_speed = 15

# Create the projectile
projectile_radius = 10
projectile_x, projectile_y = cannon_x + cannon_width // 2, cannon_y
projectile = pygame.Rect(projectile_x - projectile_radius, projectile_y - projectile_radius,
                          projectile_radius * 2, projectile_radius * 2)

# Convert angle to radians for trigonometric functions
cannon_angle_rad = math.radians(cannon_angle)

# Set initial projectile velocity components
projectile_velocity_x = projectile_speed * math.cos(cannon_angle_rad)
projectile_velocity_y = -projectile_speed * math.sin(cannon_angle_rad)

# Gravity
gravity = 0.5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the projectile
    projectile_x += projectile_velocity_x
    pygame.draw.circle(screen, PROJECTILE_COLOR, (int(projectile_x), int(projectile_y)), projectile_radius)
    projectile_y += projectile_velocity_y
    pygame.draw.circle(screen, PROJECTILE_COLOR, (int(projectile_x), int(projectile_y)), projectile_radius)
    projectile_velocity_y += gravity

    # Draw the background
    screen.fill(WHITE)

    # Draw the cannon
    pygame.draw.rect(screen, CANNON_COLOR, cannon)

    # Draw the projectile
