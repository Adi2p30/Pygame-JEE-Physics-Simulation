import pygame, sys, math

pygame.init()

FPS = 60  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
WIDTH = 400
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Verlet Simple Rigid Body System')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Particle:
    def __init__(self, x, y, m=1.0):
        self.m = m
        self.x = x
        self.y = y
        self.oldx = x - 10
        self.oldy = y
        self.newx = x
        self.newy = y
        self.ax = 0
        self.ay = 9.8

        self.selected = False
        self.fixed = False

    def update(self, delta_t):
        if self.fixed == False:
            # Collision Process
            if self.x < 0 or self.x > WIDTH:
                self.x, self.oldx = self.oldx, self.x
            if self.y < 0 or self.y > HEIGHT:
                self.y, self.oldy = self.oldy, self.y

            # Verlet Integration
            self.newx = 2.0 * self.x - self.oldx + self.ax * delta_t * delta_t
            self.newy = 2.0 * self.y - self.oldy + self.ay * delta_t * delta_t
            self.oldx = self.x
            self.oldy = self.y
            self.x = self.newx
            self.y = self.newy

        if self.selected:
            pos = pygame.mouse.get_pos()
            self.x = pos[0]
            self.y = pos[1]

        if mouse == False:
            self.selected = False

    def draw(self, surf, size):
        if self.selected == True:
            color = RED
        else:
            color = WHITE
        pygame.draw.circle(surf, color, (int(self.x), int(self.y)), size)


class Constraint:
    def __init__(self, index0, index1):
        self.index0 = index0
        self.index1 = index1
        delta_x = particles[index0].x - particles[index1].x
        delta_y = particles[index0].y - particles[index1].y
        self.restLength = math.sqrt(delta_x * delta_x + delta_y * delta_y)

    def update(self):

        delta_x = particles[self.index1].x - particles[self.index0].x
        delta_y = particles[self.index1].y - particles[self.index0].y
        deltaLength = math.sqrt(delta_x * delta_x + delta_y * delta_y)
        diff = (deltaLength - self.restLength) / (deltaLength + 0.001)

        if particles[self.index0].fixed == False:
            particles[self.index0].x += 0.5 * diff * delta_x
            particles[self.index0].y += 0.5 * diff * delta_y
        if particles[self.index1].fixed == False:
            particles[self.index1].x -= 0.5 * diff * delta_x
            particles[self.index1].y -= 0.5 * diff * delta_y

    def draw(self, surf, size):
        x0 = particles[self.index0].x
        y0 = particles[self.index0].y
        x1 = particles[self.index1].x
        y1 = particles[self.index1].y
        pygame.draw.line(surf, WHITE, (int(x0), int(y0)), (int(x1), int(y1)), size)


delta_t = 0.1
NUM_ITER = 10
mouse = False

# create particles
particles = []
for i in range(3):
    x = 20.0 * math.cos(math.radians(120) * i)
    y = 20.0 * math.sin(math.radians(120) * i)
    p = Particle(WIDTH * 0.5 + x, HEIGHT * 0.5 + y)
    if i == 0:
        p.fixed = True
    particles.append(p)


def find_particle(pos):
    for i in range(len(particles)):
        dx = particles[i].x - pos[0]
        dy = particles[i].y - pos[1]
        if (dx * dx + dy * dy) < 400:
            particles[i].selected = True
            break


constraints = []
for i in range(3):
    index0 = i
    index1 = (i + 1) % 3
    c = Constraint(index0, index1)
    constraints.append(c)

while True:
    screen.fill(BLACK)

    # particles update
    for i in range(len(particles)):
        particles[i].update(delta_t)
    # constraints update
    for n in range(NUM_ITER):
        for i in range(len(constraints)):
            constraints[i].update()

    # particles draw
    for i in range(len(particles)):
        particles[i].draw(screen, 3)
    # constraints draw
    for i in range(len(constraints)):
        constraints[i].draw(screen, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = False

    if mouse:
        pos = pygame.mouse.get_pos()
        find_particle(pos)

    pygame.display.update()
    fpsClock.tick(FPS)