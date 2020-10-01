import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# фон
rect(screen, (255, 255, 255), (0, 0, 400, 400))

# желток
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)

# рот
rect(screen, (0, 0, 0), (150, 250, 100, 20))

# глаза
circle(screen, (255, 0, 0), (150, 200), 20)
circle(screen, (0, 0, 0), (150, 200), 20, 1)
circle(screen, (255, 0, 0), (250, 200), 20)
circle(screen, (0, 0, 0), (250, 200), 20, 1)
circle(screen, (0, 0, 0), (150, 200), 10)
circle(screen, (0, 0, 0), (250, 200), 10)

# брови
polygon(screen, (0, 0, 0), [(125, 125), (175, 175), (180, 170),
                            (130, 120), (125, 125)
                            ])
polygon(screen, (0, 0, 0), [(400 - 125, 125), (400 - 175, 175), (400 - 180, 170),
                            (400 - 130, 120), (400 - 125, 125)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
