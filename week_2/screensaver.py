import pygame
import random

SCREEN_DIM = (800, 600)
SQRT = 0.5


class Vec2d:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Сумма двух векторов
        """
        return type(self)(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Разность двух векторов
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
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Polyline:
    # Класс замкнутых ломаных
    def __init__(self):
        self._points = list()
        self._speeds = list()

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

    def draw_points(self, display, style="points",
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
            ptn = list()
            ptn = [(self._points[i] + self._points[i + 1]) * SQRT,
                   self._points[i + 1],
                   (self._points[i + 1] + self._points[i + 2]) * SQRT]
            res.extend(self.get_points(ptn))
        return res


def draw_help():
    gameDisplay.fill((50, 50, 50))
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = [["F1", "Show Help"],
            ["R", "Restart"],
            ["P", "Pause/Play"],
            ["Num+", "More points"],
            ["Num-", "Less points"],
            ["", ""],
            [str(steps), "Current points"]]

    pygame.draw.lines(gameDisplay,
                      (255, 50, 50, 255), True,
                      [(0, 0), (800, 0),
                       (800, 600), (0, 600)],
                      5)

    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i))


if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps: int = 35

    polyline = Polyline()
    knot = Knot(steps)

    show_help: bool = False
    working: bool = True
    pause: bool = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    polyline = Polyline()
                    knot = Knot(steps)
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
                if event.key == pygame.K_F1:
                    show_help = not show_help
            if event.type == pygame.MOUSEBUTTONDOWN:
                polyline.add_point(Vec2d(event.pos,
                                         Vec2d(random.random() * 2,
                                               random.random() * 2)))

                knot.add_point(Vec2d(event.pos,
                                     Vec2d(random.random() * 2,
                                           random.random() * 2)))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)

        polyline.draw_points(polyline._points, gameDisplay)
        knot.draw_points(knot.get_knot(), gameDisplay, "line", color)
        if not pause:
            polyline.set_points()
            knot.set_points()
        if show_help:
            draw_help()
        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
