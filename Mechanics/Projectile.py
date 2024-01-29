import pygame, sys, math

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()
X = 300
Y = 300
# set up the window
screen = pygame.display.set_mode((1200, 400), 0, 32)
pygame.display.set_caption('Projectile Motion')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont("comicsans", 10)
delta_t = 0.2
m = 100 # Mass
g = 9.8 #Gravity
k = 0#Air Resistance

x = 0
y = 300

angle = 45
theta = math.radians(angle)

v = 100
vx = v * math.cos(theta)
vy = -v * math.sin(theta)
screen.fill(BLACK)
while True:
    screen.fill(BLACK)

    fx = -k*vx
    fy = m*g - k*vy

    vx = vx + (fx / m) * delta_t
    vy = vy + (fy / m) * delta_t

    x = x + vx * delta_t
    y = y + vy * delta_t

    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 5)
    texttoplace = "X: "+ str(round(x)) + "m\n Y:" + str(round(y))+ "m/s\n VelocityX:" + str(round(vx))+ "m/s\n VelocityY:" + str(round(vy)) + "m/s\n Potential Energy: " + str(round(abs(m * g * y))) + "J\n Kinetic Energy: " + str(round(abs(1/2 * m * (vy**2 + vx**2))))
    text = FONT.render(texttoplace, 1, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, (Y - 200) // 2)
    screen.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)