import pygame
from random import randint, random


w, h, d = 800, 600, 2
pygame.init()
screen = pygame.display.set_mode((w, h))

BLACK = pygame.Color("black")
WHITE = pygame.Color("white")

clock = pygame.time.Clock()


class Star():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.image_x = (self.x/self.z) + w//2 
        self.image_y = (self.y/self.z) + h//2
        self.trail = []

    def update(self):
        self.z -= 0.03
        if self.image_x < -w//2 or self.image_x > 3*w//2 or self.image_y < -h//2 or self.image_y > 3*h//2 :
            self.z = random()*d + 1
            self.x = randint(-w//2,w//2)
            self.y = randint(-h//2,h//2)
            self.trail = []
        self.image_x = (self.x/self.z) + w//2 
        self.image_y = (self.y/self.z) + h//2
        self.trail.append([self.image_x, self.image_y])
        if len(self.trail) > 10:
            self.trail.pop(0)

    def show(self):
        if len(self.trail)>=2:
            pygame.draw.lines(screen, (100,100,100), False, self.trail, width=1)
        # pygame.draw.line(screen, (100,100,100), (self.x + w//2 ,self.y h//2 ), (self.image_x,self.image_y), width=1)
        pygame.draw.circle(screen, WHITE, (self.image_x, self.image_y), 5 * (1-self.z/d))


def main():

    num = 100
    stars = [Star(randint(-w//2 * d,w//2 * d), randint(-h//2 * d,h//2 * d), random()*d + 1) for _ in range(num)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)

        for star in stars:
            star.update()
            star.show()

        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
