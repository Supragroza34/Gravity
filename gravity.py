import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAVITY = 0.2

class Particle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def update(self):
        self.vy += GRAVITY
        self.x += self.vx
        self.y += self.vy

        if self.y + self.size >= HEIGHT:
            self.y = HEIGHT - self.size
            self.vy *= -0.9

        if self.x <= 0 or self.x + self.size >= WIDTH:
            self.vx *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gravity Simulation")
    clock = pygame.time.Clock()

    particles = []
    for _ in range(100):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        size = random.randint(5, 20)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        particle = Particle(x, y, size, color)
        particles.append(particle)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for particle in particles:
            particle.update()
            particle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
