import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 675))

# фон
rect(screen, (254, 213, 148), (0, 0, 1000, 150))
rect(screen, (254, 213, 196), (0, 150, 1000, 150))
rect(screen, (254, 213, 148), (0, 300, 1000, 150))
rect(screen, (179, 134, 148), (0, 450, 1000, 225))

# солнце
circle(screen, (255, 255, 0), (500, 150), 56)

# первые горы
polygon(screen, (252, 142, 49), [(0, 307), (1000, 225), (928, 195),
                                 (880, 217), (840, 172), (784, 187),
                                 (744, 142), (744, 202), (500, 266)
                                 ])

polygon(screen, (252, 142, 49), [(500, 266), (536, 232), (560, 247),
                                 (592, 217), (1000, 225), (500, 266)
                                 ])

x1 = []
for i in range(97):
    x1.append((592 + i, 217 - i**2 / 136))
x1.append((688, 225))
polygon(screen, (252, 142, 49), x1)

x2 = []
for i in range(33):
    x2.append((720 - i, 120 + i**2 / 34))
x2.append((688, 225))
x2.append((744, 225))
x2.append((744, 142))
polygon(screen, (252, 142, 49), x2)

x3 = []
for i in range(25):
    x3.append((720 + i, 120 + i**2 / 26))
polygon(screen, (252, 142, 49), x3)

x4 = [(0, 307)]
for i in range(120):
    x4.append((8 + i, 277 - i**2 / 128))
x4.append((128, 262))
polygon(screen, (252, 142, 49), x4)

polygon(screen, (252, 142, 49), [(0, 307), (8, 277), (128, 262),
                                 (128, 165), (168, 180), (184, 195),
                                 (400, 255), (480, 240), (500, 266)
                                 ])

# вторые горы
pygame.draw.ellipse(screen, (172, 67, 52), [40, 285, 160, 300]) 
rect(screen, (179, 134, 148), (0, 450, 1000, 225))
polygon(screen, (172, 67, 52), [(0,  450),  (0,  337),  (16,  337),
                                (200,  435),  (240,  375),  (280,  397),
                                (320, 307), (432, 322), (500, 375),
                                (600, 360), (800, 367), (840, 307),
                                (880, 337), (920, 307), (960, 337),
                                (1000, 285), (1000, 450), (0, 465)
                                ])

x5 = []
for i in range(97):
    x5.append((696 - i, 293 + i**2 / 136))
x5.append((696, 367))
polygon(screen, (172, 67, 52), x5)

x6 = []
for i in range(53):
    x6.append((696 + i, 293 + i**2 / 74))
x6.append((696, 330))
polygon(screen, (172, 67, 52), x6)

x7 = []
for i in range(53):
    x7.append((801 - i, 367 - i**2 / 72))
x7.append((696, 330))
x7.append((696, 367))
polygon(screen, (172, 67, 52), x7)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
