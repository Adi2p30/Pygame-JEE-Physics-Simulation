
import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

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

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Projectile Motion Simulation")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

angle = 45
speed = 10

projectile = Projectile(WIDTH // 2, HEIGHT - 30, angle, speed)
all_sprites.add(projectile)

font = pygame.font.Font(None, 36)

input_angle = pygame.Rect(100, 550, 50, 32)
input_speed = pygame.Rect(250, 550, 50, 32)
button_update = pygame.Rect(400, 550, 100, 32)

color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
input_active = False
text_angle = ''
text_speed = ''
text_angle_surface = font.render(text_angle, True, color)
text_speed_surface = font.render(text_speed, True, color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_angle.collidepoint(event.pos):
                input_active = not input_active
                color = color_active if input_active else color_inactive
            elif input_speed.collidepoint(event.pos):
                input_active = not input_active
                color = color_active if input_active else color_inactive
            elif button_update.collidepoint(event.pos):
                angle = int(text_angle) if text_angle.isdigit() else angle
                speed = int(text_speed) if text_speed.isdigit() else speed
                all_sprites.empty()
                projectile = Projectile(WIDTH // 2, HEIGHT - 30, angle, speed)
                all_sprites.add(projectile)

        if event.type == pygame.KEYDOWN:
            if input_active:
                if event.key == pygame.K_RETURN:
                    input_active = not input_active
                    color = color_active if input_active else color_inactive
                elif event.key == pygame.K_BACKSPACE:
                    if text_angle:
                        text_angle = text_angle[:-1]
                    elif text_speed:
                        text_speed = text_speed[:-1]
                else:
                    if input_active:
                        text_angle += event.unicode if event.key == pygame.KMOD_SHIFT else event.unicode.lower()
                    else:
                        text_speed += event.unicode if event.key == pygame.KMOD_SHIFT else event.unicode.lower()

    all_sprites.update()

    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.draw.rect(screen, color, input_angle, 2)
    pygame.draw.rect(screen, color, input_speed, 2)
    pygame.draw.rect(screen, color_inactive, button_update, 2)

    text_angle_surface = font.render(text_angle, True, color)
    text_speed_surface = font.render(text_speed, True, color)

    width = max(200, text_angle_surface.get_width()+10)
    input_angle.w = width
    width = max(200, text_speed_surface.get_width()+10)
    input_speed.w = width

    screen.blit(text_angle_surface, (input_angle.x+5, input_angle.y+5))
    screen.blit(text_speed_surface, (input_speed.x+5, input_speed.y+5))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
sys.exit()