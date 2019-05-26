# -*- coding: utf-8 -*-
from typing import Tuple, List, Any, Union
import pygame
import random
import math

from pygame.color import Color

SCREEN_DIM: Tuple[int, int] = (800, 600)


def main():
    # Основная программа
    pygame.init()
    gameDisplay: object = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps: int = 35
    working: bool = True
    points: List[Tuple[int, int]] = []
    speeds: List[Tuple[Union[int, Any], Union[int, Any]]] = []
    show_help: bool = False
    pause: bool = True

    hue: int = 0
    color: Color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
                if event.key == pygame.K_F1:
                    show_help = not show_help

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)
                speeds.append((random.random() * 2,
                               random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        draw_points(points)
        draw_points(get_knot(points, steps), "line", 3, color)
        if not pause:
            set_points(points, speeds)
        if show_help:
            draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)


class Vec2d:
    def __init__(self, x, y, v, k):
        self.x = x
        self.y = y
        self.v = v
        self.k = k

    def __add__(self):
        # сумма двух векторов
        return self.x[0] + self.y[0], self.x[1] + self.y[1]

    def __sub__(self):
        return self.x[0] - self.y[0], self.x[1] - self.y[1]

    def __mul__(self):
        return self.v[0] * self.k, self.v[1] * self.k

    def len(self):
        return math.sqrt(self.x[0] *
                         self.x[0] +
                         self.x[1] *
                         self.x[1])

    def int_pair(self) -> tuple:
        return self.__sub__(self.y, self.x)


class Polyline:
    pass


class Knot(Polyline):
    pass


# Методы для работы с векторами


def sub(x, y):
    # разность двух векторов
    return x[0] - y[0], x[1] - y[1]


def add(x, y):
    # сумма двух векторов
    return x[0] + y[0], x[1] + y[1]


def length(x):
    # длинна вектора
    return math.sqrt(x[0] * x[0] + x[1] * x[1])


def mul(v, k):
    # умножение вектора на число
    return v[0] * k, v[1] * k


def scal_mul(v, k):
    # скалярное умножение векторов
    return v[0] * k, v[1] * k


def vec(x, y):
    # создание вектора по началу (x) и концу (y) направленного отрезка
    return sub(y, x)


# "Отрисовка" точек
def draw_points(points, style="points", width=3, color=(255, 255, 255)):
    if style == "line":
        for p_n in range(-1, len(points) - 1):
            pygame.draw.line(gameDisplay,
                             color,
                             (int(points[p_n][0]),
                              int(points[p_n][1])),
                             (int(points[p_n + 1][0]),
                              int(points[p_n + 1][1])),
                             width)

    elif style == "points":
        for p in points:
            pygame.draw.circle(gameDisplay, color,
                               (int(p[0]), int(p[1])), width)


def get_point(points, alpha, deg=None):
    # Сглаживание ломаной
    if deg is None:
        deg = len(points) - 1
    if deg == 0:
        return points[0]
    return add(mul(points[deg], alpha),
               mul(get_point(points, alpha, deg - 1),
                   1 - alpha))


def get_points(base_points, count):
    alpha = 1 / count
    res = []
    for i in range(count):
        res.append(get_point(base_points, i * alpha))
    return res


def get_knot(points, count):
    if len(points) < 3:
        return []
    res = []
    for i in range(-2, len(points) - 2):
        ptn = []
        ptn.append(mul(add(points[i], points[i + 1]), 0.5))
        ptn.append(points[i + 1])
        ptn.append(mul(add(points[i + 1], points[i + 2]), 0.5))

        res.extend(get_points(ptn, count))
    return res


def draw_help():
    # Отрисовка справки
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = []
    data.append(["F1", "Show Help"])
    data.append(["R", "Restart"])
    data.append(["P", "Pause/Play"])
    data.append(["Num+", "More points"])
    data.append(["Num-", "Less points"])
    data.append(["", ""])
    data.append([str(steps), "Current points"])

    pygame.draw.lines(gameDisplay,
                      (255, 50, 50, 255), True,
                      [(0, 0),
                       (800, 0),
                       (800, 600),
                       (0, 600)],
                      5)

    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


def set_points(points, speeds):
    # Персчитывание координат опорных точек
    for p in range(len(points)):
        points[p] = add(points[p], speeds[p])
        if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
            speeds[p] = (- speeds[p][0], speeds[p][1])
        if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
            speeds[p] = (speeds[p][0], -speeds[p][1])


if __name__ == "__main__":
    main()
