import pygame
from pygame.draw import *
from random import randint

print('What is your name?')
name = input()
pygame.init()

image = pygame.image.load('fly.png')
points_for_fly = 5
points_for_ball = 1
number_for_fly = 10
time_of_fly = 5
time_of_ball = 10
number_of_balls = 5
FPS = 30
height = 450
length = 600
rmax = 50
rmin = 20
v_0 = 10
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, WHITE]
screen = pygame.display.set_mode((length, height + 55))


class Ball:
    '''
    Это класс, описывающий шарик
    '''

    def __init__(self, x, y, r, color, v_x, v_y, time):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.v_x = v_x
        self.v_y = v_y
        self.time = time

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_r(self):
        return self.r

    def get_color(self):
        return self.color

    def get_v_x(self):
        return self.v_x

    def get_v_y(self):
        return self.v_y

    def get_time(self):
        return self.time

    def time_goes(self):
        self.time += 1

    def moving(self, h, l):
        if self.x <= self.r:
            self.v_x = abs(self.v_x)
        if self.x >= l - self.r:
            self.v_x = -abs(self.v_x)
        if self.y <= self.r:
            self.v_y = abs(self.v_y)
        if self.y >= h - self.r:
            self.v_y = - abs(self.v_y)
        self.x += self.v_x
        self.y += self.v_y

    def draw(self):
        circle(screen, BLACK, (self.x, self.y), self.r, 1)
        circle(screen, self.color, (self.x, self.y), self.r)
        

class Fly:
    '''
    Это класс, описывающий муху
    '''

    def __init__(self, x, y, time, size=50):
        Fly.x = x
        Fly.y = y
        Fly.time = time
        Fly.size = size

    def get_time(self):
        return Fly.time

    def get_x(self):
        return Fly.x

    def get_y(self):
        return Fly.y

    def get_size(self):
        return Fly.size
    
    def moving(self, v_fly, h, l):
        Fly.v_x = randint(-v_fly, v_fly)
        Fly.v_y = randint(-v_fly, v_fly)
        if Fly.x <= v_fly:
            Fly.v_x = abs(Fly.v_x)
        if Fly.x >= l - Fly.size - v_fly:
            Fly.v_x = -abs(Fly.v_x)
        if Fly.y <= v_fly:
            Fly.v_y = abs(Fly.v_y)
        if Fly.y >= h - Fly.size - v_fly:
            Fly.v_y = -abs(Fly.v_y)
        Fly.x += Fly.v_x
        Fly.y += Fly.v_y

    def time_goes(self):
        Fly.time += 1

    def draw(self, image_fly):
        image_fly = pygame.transform.scale(image_fly, (Fly.size, Fly.size))
        image_rect = image.get_rect(topleft=(Fly.x, Fly.y))
        screen.blit(image_fly, image_rect)


def new_ball():
    '''
    Функция возвращает объект класса Ball со случайными характеристиками
    '''
    x1 = randint(rmax, length - rmax)
    y1 = randint(rmax, height - rmax)
    r1 = randint(rmin, rmax)
    v_x1 = randint(-v_0, v_0)
    v_y1 = randint(-v_0, v_0)
    color = COLORS[randint(0, 6)]
    return Ball(x1, y1, r1, color, v_x1, v_y1, 0)


def new_fly():
    '''
    Функция возвращает объект класса Fly со случайными размером и координатами
    '''
    size_fly = randint(40, 60)
    x_fly = randint(0, length - size_fly)
    y_fly = randint(0, height - size_fly)
    return Fly(x_fly, y_fly, 0, size_fly) 


def display_score(n):
    '''
    функция выводит счет n на экран
    '''
    text = font.render("Score: " + str(n), 1, (0, 255, 0))
    place = text.get_rect(center=(length/2, height + 30))
    sc.blit(text, place)


def hit_ball(shar, x_mouse, y_mouse):
    '''
    Функция возвращает True, если игрок попал в шарик
    иначе возвращает False
    '''
    delta_x = shar.get_x() - x_mouse
    delta_y = shar.get_y() - y_mouse
    if delta_x**2 + delta_y**2 <= shar.get_r()**2:
        return True
    else:
        return False


def hit_fly(fly_1, x_mouse, y_mouse):
    '''
    Функция возвращает True, если игрок попал в муху
    иначе возвращает False
    '''
    popal_x = fly_1.get_x() <= x_mouse <= fly_1.get_x() + fly_1.get_size()
    popal_y = fly_1.get_y() <= y_mouse <= fly_1.get_y() + fly_1.get_size()
    if popal_x and popal_y:
        return True
    else:
        return False


pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
trigger_of_fly = False
sc = pygame.display.set_mode((length, height + 55))
sc.fill((255, 255, 255))
font = pygame.font.Font(None, 72)  
balls = [new_ball() for i in range(number_of_balls)]
fly = Fly(0, 0, -1)
pygame.mixer.music.load('Ohota.mp3')
pygame.mixer.music.play()

while not finished:
    remainder = score % number_for_fly
    if (remainder <= 1) and (score != remainder) and not trigger_of_fly:
        fly = new_fly()
        trigger_of_fly = True
    if -1 < fly.get_time() < time_of_fly * FPS:
        fly.time_goes()
        fly.draw(image)
        fly.moving(v_0, height, length)
        rect(screen, GREEN, (0, height, length*(1 - fly.get_time()/(time_of_fly * FPS)), 5))

    for j, ball in enumerate(balls):
        if ball.get_time() == time_of_ball * FPS:
            balls[j] = new_ball()
        ball.draw()
        ball.time_goes()
        ball.moving(height, length)

    rect(screen, WHITE, (0, height, length, 55))
    display_score(score)
    pygame.display.update()
    screen.fill(BLACK)
    clock.tick(FPS)
    
    for event in pygame.event.get():
        trigger_of_balls = False
        if event.type == pygame.QUIT:
            finished = True
            with open("Scores.txt", "a") as file:
                file.write(name + ': ' + str(score) + '\n')
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_m, y_m = event.pos
            if 0 < fly.get_time() < time_of_fly * FPS:
                if hit_fly(fly, x_m, y_m):
                    score += points_for_fly
                    fly = Fly(0, 0, -1)
                    trigger_of_fly = False
            for j in range(number_of_balls - 1, -1, -1):
                if hit_ball(balls[j], x_m, y_m) and not trigger_of_balls:
                    score += points_for_ball
                    balls[j] = new_ball()
                    trigger_of_balls = True

pygame.quit()
