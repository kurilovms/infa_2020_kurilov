import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 700))

color_of_sky = (0, 51, 102)
color_of_ground = (18, 53, 36)
color_of_moon = (253, 245, 230)
color_of_ufo_light = (250, 250, 250)
color_of_ufo_glass = (230, 230, 230)
color_of_ufo_korpus = (190, 190, 190)
color_of_ufo_fonar = (253, 233, 16)
color_of_alien = (187, 240, 51)
WHITE = (255, 255, 255)


def sky_and_ground(surface_sky_and_ground, color_sky, color_ground, height):
    '''
    Функция рисует небо
    surface_sky_and_ground - объект pygame.Surface
    color_sky - цвет неба, заданный в формате, подходящем для pygame.Color
    height - высота верхней части экрана над уровнем земли
    color_ground - цвет земли, заданный в формате, подходящем для pygame.Color
    '''
    pygame.draw.polygon(surface_sky_and_ground, color_sky,
                        [(0, 0), (600, 0), (600, height), (0, height)]
                        )
    pygame.draw.polygon(surface_sky_and_ground, color_ground,
                        [(0, height), (600, height), (600,700), (0, 700)]
                        )


def moon(surface_moon, color_moon, x_moon, y_moon, r_moon):
    '''
    Функция рисует Луну
    surface_moon - объект pygame.Surface
    x_moon - координата центра Луны по оси x
    y_moon - координата центра Луны по оси y
    '''
    pygame.draw.circle(surface_moon, color_moon, [x_moon, y_moon], r_moon)


def clouds(surface_clouds, number_of_pic, height, alpha_clouds):
    '''
    Функция рисует облака
    surface_clouds - объект pygame.Surface
    number_of_pic - номер одного из трех видов облаков (1 or 2 or 3)
    height - высота верхней части экрана над уровнем земли
    alpha_clouds - коэффициент непрозрачности облаков (0 <= alpha <= 255)
    '''
    image = pygame.image.load('clouds' + str(number_of_pic) + '.jpg')
    image = pygame.transform.scale(image, (600, height))
    image_rect=image.get_rect()
    image.set_alpha(alpha_clouds)
    surface_clouds.blit(image, image_rect)


def ufo(surface_ufo, x_ufo, y_ufo, k_ufo, color_ufo_light, color_ufo_glass,
        color_ufo_korpus, color_ufo_fonar, alpha_ufo
        ):
    '''
    surface_ufo - объект pygame.Surface
    x - координата по оси x самой левой точки
    летающей тарелки
    y - координата по оси y самой верхней точки
    летающей тарелки
    k - коэффициент пропорциональности линейных размеров
    color_ufo_light - цвет света под летающей тарелкой,
    заданный в формате, подходящем для pygame.Color
    color_ufo_glass - цвет стекла летающей тарелки,
    заданный в формате, подходящем для pygame.Color
    color_ufo_korpus - цвет корпуса летающей тарелки,
    заданный в формате, подходящем для pygame.Color
    color_ufo_fonar - цвет фонарей на летающей тарелке,
    заданный в формате, подходящем для pygame.Color
    alpha_ufo - коэффициент непрозрачности света под летающей тарелкой
    '''
    treu = pygame.Surface((int(240*k_ufo), int(150*k_ufo)))
    # тут я исправил то, что теперь свет может быть любого цвета
    # (в изначальном варианте нельзя было брать (255, 255, 255))
    if color_ufo_light == (0, 0, 0):
        treu.fill(WHITE)
        treu.set_colorkey(WHITE)
    else:
        treu.fill((0, 0, 0))
        treu.set_colorkey((0, 0, 0))
    pygame.draw.polygon(treu, color_ufo_light,
                        [(int(125*k_ufo), 0), (int(240*k_ufo),
                         int(150*k_ufo)), (int(10*k_ufo), int(150*k_ufo))]
                        )
    treu.set_alpha(alpha_ufo)
    # ранее y задавало верхнюю точку корпуса, а сейчас всей тарелки
    surface_ufo.blit(treu, (x_ufo, int(y_ufo+15*k_ufo)))
    pygame.draw.ellipse(surface_ufo, color_ufo_korpus,
                        (x_ufo, int(y_ufo+15*k_ufo),
                         int(250*k_ufo), int(75*k_ufo))
                        )
    pygame.draw.ellipse(surface_ufo, color_ufo_glass,
                        (int(x_ufo+30*k_ufo), y_ufo,
                         int(190*k_ufo), int(60*k_ufo))
                        )
    pygame.draw.ellipse(surface_ufo, color_ufo_fonar,
                        (int(x_ufo+110*k_ufo), int(y_ufo+65*k_ufo),
                         int(30*k_ufo), int(18*k_ufo))
                        )
    pygame.draw.ellipse(surface_ufo, color_ufo_fonar,
                        (int(x_ufo+60*k_ufo), int(y_ufo+60*k_ufo),
                         int(30*k_ufo), int(18*k_ufo)))
    pygame.draw.ellipse(surface_ufo, color_ufo_fonar,
                        (int(x_ufo+160*k_ufo), int(y_ufo+60*k_ufo),
                         int(30*k_ufo), int(18*k_ufo))
                        )
    pygame.draw.ellipse(surface_ufo, color_ufo_fonar,
                        (int(x_ufo+15*k_ufo), int(y_ufo+45*k_ufo),
                         int(30*k_ufo), int(18*k_ufo))
                        )
    pygame.draw.ellipse(surface_ufo, color_ufo_fonar,
                        (int(x_ufo+210*k_ufo), int(y_ufo+45*k_ufo),
                         int(30*k_ufo), int(18*k_ufo))
                        )


def alien(surface_alien, x_alien, y_alien, k_alien, color_alien,
          color_apple='surprise', smotr ='right'
          ):
    '''
    surface_alien - объект pygame.Surface
    x_alien - координата по оси x самой левой точки инопланетянина
    y_alien - координата по оси y верхней точки инопланетянина
    k_alien - коэффициент пропорциональности линейных размеров
    color_apple - цвет яблока инопланетянина
    (по-умолчанию - случайный цвет с нулевым значением blue)
    smotr - направление взгляда инопланетяна
    (по-умолчанию вправо, если задать параметр 'left', то будет смотреть влево)
    '''
    # сейчас цвет яблока не обязательно рандомный
    if (color_apple == 'surprise'):
        color_apple = (randint(128, 255), randint(0, 128), 0)
    al = pygame.Surface((int(600), int(700)))
    # раньше нельзя было сделать яблоко или инопланетянина белыми
    if (color_alien != (255, 255, 254)) and (color_apple != (255, 255, 254)):
        al.fill((254, 254, 254))
        al.set_colorkey((254, 254, 254))
    elif (color_alien == (10, 0, 0)):
        al.fill((20, 0, 0))
        al.set_colorkey((20, 0, 0))
    else:
        al.fill((10, 0, 0))
        al.set_colorkey((10, 0, 0))
    # теперь x_alien и y_alien это минимальные координаты по осям x и y
    x_alien = x_alien+ 48*k_alien
    y_alien = y_alien + 139*k_alien
    # body
    pygame.draw.ellipse(al, color_alien, (x_alien, y_alien, int(k_alien*50), int(k_alien*105)))
    # left_arm
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien-30*k_alien), int(y_alien+5*k_alien), int(k_alien*40), int(k_alien*40))
                        )
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien-42*k_alien), int(y_alien+35*k_alien), int(k_alien*25), int(k_alien*25))
                        )
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien-35*k_alien), int(y_alien+55*k_alien), int(k_alien*20), int(k_alien*20))
                        )
    # right_arm
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien+47*k_alien), int(y_alien+5*k_alien), int(k_alien*40), int(k_alien*40))
                        )
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien+70*k_alien), int(y_alien+35*k_alien), int(k_alien*25), int(k_alien*25))
                        )
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien+88*k_alien), int(y_alien+50*k_alien), int(k_alien*25), int(k_alien*17))
                        )
    # apple
    pygame.draw.circle(al, color_apple,
                       [int(x_alien+120*k_alien), int(y_alien+45*k_alien)], int(k_alien*22)
                       )
    pygame.draw.line(al, (0, 0, 0),
                     [int(x_alien+125*k_alien), int(y_alien+30*k_alien)],
                     [int(x_alien+130*k_alien), int(y_alien+15*k_alien)], 2
                     )
    pygame.draw.polygon(al, (0, 230, 0),
                        [(int(x_alien+126*k_alien), int(y_alien+19*k_alien)),
                         (int(x_alien+138*k_alien), int(y_alien+10*k_alien)),
                         (int(x_alien+132*k_alien),int(y_alien+15*k_alien))]
                        )
    # left_leg
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien-15*k_alien), int(y_alien+75*k_alien), int(k_alien*40), int(k_alien*40))
                        )
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien-20*k_alien), int(y_alien+105*k_alien), int(k_alien*30), int(k_alien*30))
                        )
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien-22*k_alien), int(y_alien+125*k_alien), int(k_alien*20), int(k_alien*20))
                        )
    pygame.draw.ellipse(al, color_apple,
                        (int(x_alien-20*k_alien), int(y_alien+145*k_alien), int(k_alien*27), int(k_alien*15))
                        )
    # right_leg
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien+30*k_alien), int(y_alien+75*k_alien), int(k_alien*40), int(k_alien*40))
                        )
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien+40*k_alien), int(y_alien+105*k_alien), int(k_alien*30), int(k_alien*30))
                        )
    pygame.draw.ellipse(al, color_alien,
                        (int(x_alien+38*k_alien), int(y_alien+125*k_alien), int(k_alien*20), int(k_alien*20))
                        )
    pygame.draw.ellipse(al, color_apple,
                        (int(x_alien+40*k_alien), int(y_alien+145*k_alien), int(k_alien*27), int(k_alien*15))
                        )
    # head
    image = pygame.image.load('head.png')
    image = pygame.transform.scale(image, (int(150*k_alien), int(146*k_alien)))
    image_rect = image.get_rect(topleft=(int(x_alien-63*k_alien), int(y_alien-125*k_alien)))
    al.blit(image, image_rect)
    # left_ear
    pygame.draw.circle(al, color_alien, [int(x_alien-30*k_alien), int(y_alien-95*k_alien)], int(k_alien*12))
    pygame.draw.circle(al, color_apple, [int(x_alien-40*k_alien), int(y_alien-110*k_alien)], int(k_alien*8))
    # right_ear
    pygame.draw.circle(al, color_alien, [int(x_alien+20*k_alien), int(y_alien-113*k_alien)], int(k_alien*12))
    pygame.draw.circle(al, color_apple, [int(x_alien+15*k_alien), int(y_alien-131*k_alien)], int(k_alien*8))
    
    if (smotr == 'left'):
        al = pygame.transform.flip(al, True, False)
    surface_alien.blit(al, (0, 0))


sky_and_ground(screen, color_of_sky, color_of_ground, 400)
moon(screen, color_of_moon, 450, 100, 60)
clouds(screen, 2, 400, 100)
ufo(screen, 40, 300, 1, color_of_ufo_light,
    color_of_ufo_glass, color_of_ufo_korpus, color_of_ufo_fonar, 100)
ufo(screen, 400, 400, 0.7, color_of_ufo_light,
    color_of_ufo_glass, color_of_ufo_korpus, color_of_ufo_fonar, 100)
ufo(screen, 70, 450, 0.8, color_of_ufo_light,
    color_of_ufo_glass, color_of_ufo_korpus, color_of_ufo_fonar, 100)
alien(screen, 252, 261, 1, color_of_alien)
alien(screen, 402, 361, 0.8, color_of_alien, color_apple = WHITE)
alien(screen, 402, 461, 0.5, color_of_alien, smotr='left')

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
