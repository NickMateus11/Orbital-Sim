from numpy.core.numeric import array_equal
import pygame
import numpy as np
import random


w, h = 800, 800
pygame.init()
screen = pygame.display.set_mode((w, h))

BLACK = pygame.Color("black")
WHITE = pygame.Color("white")

clock = pygame.time.Clock()

G = 10


class Body():
    def __init__(self, pos, mass):
        self.pos = np.array(pos, dtype=np.float64)
        self.mass = mass
        self.vel = np.zeros(shape=2, dtype=np.float64)
        self.trail = []
    
    def update(self, other):
        self.pos += self.vel
        self.trail.append(list(self.pos))
        if len(self.trail)>50:
            self.trail.pop(0)

        r = np.linalg.norm(self.pos-other.pos)
        v_prime = G * (other.mass / r**3) * (other.pos-self.pos)
        self.vel += v_prime
    
    def draw(self):
        pygame.draw.circle(screen, WHITE, self.pos, min(2*self.mass,30))
        if len(self.trail)>=2:
            pygame.draw.lines(screen, WHITE, False, self.trail, width=1)
    
    def copy(self):
        return Body(self.pos, self.mass)


def main():

    body1 = Body((w//2,h//2), 500)
    body2 = Body((w//2,h//4), 2)
    body3 = Body((w//2,4*h//5), 5)
    body4 = Body((4*w//5,h//2), 5)

    system = [body1,body2,body3,body4]

    body2.vel = (2,0)
    body3.vel = (-2.8,0)
    body4.vel = (0,-2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        snapshot = [b.copy() for b in system]
        for i in range(len(system)):
            system[i].draw()
            for j in range(len(system)):
                if i == j: continue
                system[i].update(snapshot[j])

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
