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
        self.is_exploded = False

    def update(self):
        if not self.is_exploded:
            self.vy += GRAVITY
            self.x += self.vx
            self.y += self.vy

            if self.y + self.size >= HEIGHT:
                self.y = HEIGHT - self.size
                self.vy *= -0.9

            if self.x <= 0 or self.x + self.size >= WIDTH:
                self.vx *= -1
        else:
            self.size -= 0.5
            if self.size <= 0:
                self.is_exploded = False
                self.size = random.randint(5, 20)
                self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                self.vx = random.uniform(-1, 1)
                self.vy = random.uniform(-1, 1)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Gravity and Explosion")
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for particle in particles:
                        if particle.x - particle.size < event.pos[0] < particle.x + particle.size and \
                                particle.y - particle.size < event.pos[1] < particle.y + particle.size:
                            particle.is_exploded = True

        screen.fill(BLACK)

        for particle in particles:
            particle.update()
            particle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
