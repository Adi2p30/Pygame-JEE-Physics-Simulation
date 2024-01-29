import pygame, sys, math

pygame.init()

FPS = 70  # frames per second setting
fpsClock = pygame.time.Clock()

#FONT Positions
X = 200
Y = 300
FONT = pygame.font.SysFont("comicsans", 10)
TitleFONT = pygame.font.SysFont("comicsans", 20)

# set up the window
screen = pygame.display.set_mode((800, 400), 0, 32)
pygame.display.set_caption('Mass Spring System')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

delta_t = 0.1
m = 1
k = 0.5  # Spring Constant
c = 0.2 # Damping Constant
x = 500
y = 250

vx = 10
vy = 0

while True:
    # screen.fill(BLACK)
    fx = 0
    fy = -k * (y-150) -c * vy
    vy = vy + (fy / m) * delta_t
    y = y + vy * delta_t
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 10)
    texttoplace = "Position: "+ str(round(y*-1 + 150)) + "m\n Velocity:" + str(round(vy)) +"m/s\n Potential Energy: " + str(round(abs(k * abs(y*-1 + 150) * abs(y*-1 + 150)/2))) + "J\n Kinetic Energy: " + str(round(abs(1/2 * m * vy * vy))) + "J\nTime Period: " + str(round(2 * 3.14 * (m/k)**0.5)) + "seconds"
    text = FONT.render("K = " + str(k) + "\n M = " + str(m) + "\n C = " + str(c), 1, RED)
    text1 = FONT.render(texttoplace , 1, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, (Y - 200) // 2)
    textRect1 = text1.get_rect()
    textRect1.center = (X // 2, Y // 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(text, textRect)
    screen.blit(text1, textRect1)
    pygame.display.update()
    fpsClock.tick(FPS)