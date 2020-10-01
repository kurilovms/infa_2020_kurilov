import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 675))


def bird(k, x, y):
    m = [(x, y), (x + k*87, y - k*50)]
    for j in range(78):
        m.append((x + k*87 - k*j, y - k*50 + k*33 * j**2/(77**2)))
    for j in range(-82, 1):
        m.append((x - k*72 - k*j, y - k*50 + k*33 * j**2 / (82**2)))
    for j in range(-3, 1):
        m.append((x - k*77 + k*10 * j**2 / 9, y - k*47 + k*j))
    for j in range(10):
        m.append((x - k*77 + k * j**2 / 8, y - k*47 + k*j))
    polygon(screen, (66, 33, 11), m)


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

# третьи горы
polygon(screen, (48, 16, 38), [(0, 360), (120, 390), (240, 510),
                               (320, 600), (320, 675), (0, 675),
                               (0, 360)
                               ])

x8 = []
for i in range(181):
    x8.append((500 - i, 660 - i**2 / 540))
x8.append((320, 675))
x8.append((500, 675))
polygon(screen, (48, 16, 38), x8)

polygon(screen, (48, 16, 38), [(500, 659), (700, 550), (760, 590),
                               (760, 675), (500, 675), (500, 659)])

x9 = []
for i in range(-60, 1):
    x9.append((820 + i, 610 - i**2 / 180))
x9.append((820, 675))
x9.append((760, 675))
polygon(screen, (48, 16, 38), x9)

x10 = []
for i in range(121):
    x10.append((1000 - i, 430 + i**2 / 144))
x10.append((880, 675))
x10.append((1000, 675))
polygon(screen, (48, 16, 38), x10)

x11 = []
for i in range(61):
    x11.append((820 + i, 610 - i**2 / 45))
x11.append((880, 675))
x11.append((820, 675))
polygon(screen, (48, 16, 38), x11)

# птицы сверху
bird(0.45, 400, 245)
bird(0.45, 500, 246)
bird(0.45, 510, 300)
bird(0.45, 440, 324)

# птицы снизу
bird(0.55, 800, 560)
bird(0.3, 820, 500)
bird(0.4, 700, 520)
bird(0.45, 660, 460)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
