import pygame
from pygame.draw import *


def display(surface, color):
    '''
    Функция закрашивает экран
    surface - объект pygame.Surface
    color - цвет, заданный в формате, подходящем для pygame.Color
    '''
    rect(surface, color, (0, 0, 400, 400))


def eye(surface, color_eye, x_eye, y_eye, r_eye):
    '''
    Функция рисует белок глаза
    surface - объект pygame.Surface
    color_eye - цвет, заданный в формате, подходящем для pygame.Color
    x_eye - координата по оси x центра круга
    y_eye - координата по оси y центра круга
    r_eye - радиус круга
    '''
    circle(surface, color_eye, (x_eye, y_eye), r_eye)


def pupil(surface, color_pupil, x_pupil, y_pupil, r_pupil):
    '''
    Функция рисует зрачок
    surface - объект pygame.Surface
    color_pupil - цвет, заданный в формате, подходящем для pygame.Color
    x_pupil - координата по оси x центра круга
    y_pupil - координата по оси y центра круга
    r_pupil - радиус круга
    '''
    circle(surface, color_pupil, (x_pupil, y_pupil), r_pupil)


def mouth(surface, color_mouth, x_mouth, y_mouth, Delta_x_mouth, Delta_y_mouth):
    '''
    Функция рисует рот
    surface - объект pygame.Surface
    color_mouth - цвет, заданный в формате, подходящем для pygame.Color
    x_mouth - координата по оси x левого верхнего угла
    y_mouth - координата по оси y левого верхнего угла
    Delta_x_mouth - ширина рта
    Delta_y_mouth - высота рта
    '''
    rect(surface, color_mouth, (x_mouth, y_mouth, Delta_x_mouth, Delta_y_mouth))


def left_eyebrow(surface, color_left_eyebrow, x_left_eyebrow, y_left_eyebrow, k_left_eyebrow):
    '''
    Функция рисует левую бровь
    surface - объект pygame.Surface
    color_left_eyebrow - цвет, заданный в формате, подходящем для pygame.Color
    x_left_eyebrow- координата по оси x правого нижнего края
    y_left_eyebrow- координата по оси y правого нижнего края
    k_left_eyebrow - коэффициент пропорциональности, размеры брови умножаются на k_left_eyebrow
    '''
    polygon(surface, color_left_eyebrow, [(x_left_eyebrow, y_left_eyebrow),
                                          (x_left_eyebrow + 3*k_left_eyebrow, y_left_eyebrow - 10*k_left_eyebrow),
                                          (x_left_eyebrow - 67*k_left_eyebrow, y_left_eyebrow - 20*k_left_eyebrow),
                                          (x_left_eyebrow - 70*k_left_eyebrow, y_left_eyebrow - 10*k_left_eyebrow)
                                          ])


def right_eyebrow(surface, color_right_eyebrow, x_right_eyebrow, y_right_eyebrow, k_right_eyebrow):
    '''
    Функция рисует левую бровь
    surface - объект pygame.Surface
    color_right_eyebrow - цвет, заданный в формате, подходящем для pygame.Color
    x_right_eyebrow- координата по оси x левого нижнего края
    y_right_eyebrow- координата по оси y левого нижнего края
    k_right_eyebrow - коэффициент пропорциональности, размеры брови умножаются на k_left_eyebrow
    '''
    polygon(surface, color_right_eyebrow, [(x_right_eyebrow, y_right_eyebrow),
                                           (x_right_eyebrow + 60*k_right_eyebrow, y_right_eyebrow - 20*k_right_eyebrow),
                                           (x_right_eyebrow + 58*k_right_eyebrow, y_right_eyebrow - 30*k_right_eyebrow),
                                           (x_right_eyebrow - 2*k_right_eyebrow, y_right_eyebrow - 10*k_right_eyebrow)
                                           ])


def head(surface, color_head, x_head, y_head, r_head):
    '''
    Функция рисует голову смайлика
    surface - объект pygame.Surface
    color_head - цвет, заданный в формате, подходящем для pygame.Color
    x_head - координата по оси x центра круга
    y_head - координата по оси y центра круга
    r_head - радиус круга
    '''
    circle(surface, color_head, (x_head, y_head), r_head)


pygame.init()
FPS = 30

screen = pygame.display.set_mode((400, 400))

display(screen, (255, 255, 255))
head(screen, (255, 255, 0), 200, 175, 100)
eye(screen, (255, 0, 0), 150, 140, 20)
pupil(screen, (0, 0, 0), 150, 140, 6)
eye(screen, (255, 0, 0), 245, 140, 15)
pupil(screen, (0, 0, 0), 245, 140, 6)
mouth(screen, (0, 0, 0), 150, 200, 100, 10)
left_eyebrow(screen, (0, 0, 0), 180, 135, 1)
right_eyebrow(screen, (0, 0, 0), 215, 140, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
