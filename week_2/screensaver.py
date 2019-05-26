from typing import Tuple, List, Union
import pygame
# import random

SCREEN_DIM: Tuple[int, int] = (800, 600)
SQRT: float = 0.5


class Vect2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Сумма двух векторов
        :rtype: Tuple[Union[int, float], Union[int, float]]
        """
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Разность двух векторов
        :rtype: Tuple[Union[int, float], Union[int, float]]
        """
        return type(self)(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        """
        Умножение на скаляр
        """
        return type(self)(k * self.x, k * self.y)

    def scal_mul(self, k):
        # скалярное умножение векторов
        return sum(k * self.x, k * self.y)

    def __len__(self):
        """
        Величина вектора
        :rtype: float
        """
        return (self.x**2 + self.y**2) ** SQRT

    def int_pair(self):
        """
        Получение пары целых чисел.
        :rtype: Tuple[int, int]
        """
        return int(self.x), int(self.y)

    def __str__(self):
        return f"Vec2d({self.x}, {self.y})"

    def __repr__(self):
        return f"Vec2d({self.x}, {self.y})"


class Polyline:

    def __init__(self):
        self._points = []
        self._speeds = []

    def add_point(self, point):
        self._points.append(point)

    def delete_point(self):
        self._points.pop()

    def set_points(self):
        _width = SCREEN_DIM[0]
        _height = SCREEN_DIM[1]
        for p in range(len(self._points)):
            self._points[p] = self._points[p] + self._speeds[p]
            if self._points[p][0] > _width or self._points[p][0] < 0:
                self._speeds[p][0] = -self._speeds[p][0]
            if self._points[p][1] > _height or self._points[p][1] < 0:
                self._speeds[p][1] = -self._speeds[p][1]

    def draw_points(self, style="points", display,
                    color=(255, 255, 255), width=3):
        """
        Отрисовка точек
        """
        if style == "line":
            for p in range(-1, len(self._points) - 1):
                pygame.draw.line(display, color,
                                 self._points[p].int_pair(),
                                 self._points[p + 1].int_pair(),
                                 width)
        elif style == "points":
            for p in self._points:
                pygame.draw.circle(display, color,
                                   p.int_pair(),
                                   width)


class Knot(Polyline):
    # Сглаживание ломаной
    Knots = []

    def __init__(self, count):
        super().__init__()
        self.count = count
        Knot.Knots.append(self)

    def add_point(self, point):
        super().add_point(point)
        self.get_knot()

    def delete_point(self):
        super().delete_point()
        self.get_knot()

    def set_points(self):
        super().set_points()
        self.get_knot()

    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self.get_point(points, alpha,
                                                    deg - 1) * (1 - alpha)

    def get_points(self, base_points):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self):
        if len(self._points) < 3:
            return []
        res = []
        for i in range(-2, len(self._points) - 2):
            ptn = [(self._points[i] + self._points[i + 1]) * 0.5, self._points[i + 1],
                   (self._points[i + 1] + self._points[i + 2]) * 0.5]
            res.extend(self.get_points(ptn))
        return res
