import pygame
from pygame.draw import *
from random import randint
from math import sqrt
pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 450))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]


def rand_param():
    x1 = randint(100,500)
    y1 = randint(100,350)
    r1 = randint(30,100)
    v_x1 = randint(-10,10)
    v_y1 = randint(-10,10)
    color = COLORS[randint(0, 6)]
    return x1, y1, r1, color, v_x1, v_y1


def new_ball(x2, y2, r2, color2):
    circle(screen, color2, (x2, y2), r2)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
number = 0

while not finished:
    x, y, r, color, v_x, v_y = rand_param()
    sharik_poyman = False
    i=0
    while (not sharik_poyman) and (i <= 100):
        circle(screen, color, (x, y), r)
        pygame.display.update()
        screen.fill(BLACK)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_m, y_m = event.pos
                if (x - x_m)**2 + (y - y_m)**2 <= r**2:
                    number+=1
                    print(number)
                    sharik_poyman = True
        i+=1
        if (x <= r) or (x >= 600 - r):
            v_x = -v_x
        if (y <= r) or (y >= )
        x=x + v_x
        y=y + v_y

pygame.quit()
