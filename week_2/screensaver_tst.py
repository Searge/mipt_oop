from typing import Tuple, List
import pygame
import random

SCREEN_DIM: Tuple[int, int] = (800, 600)


def main():
    # Основная программа
    pygame.init()

    # <class 'pygame.Surface'>
    gameDisplay: object = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps: int = 35
    points: List[Tuple[int, int]] = []
    speeds: List[Tuple[float, float]] = []
    # show_help: bool = False
    working: bool = True
    pause: bool = True

    print("\nTesting:\n=== === === === === ===\n\n")

    hue: int = 0
    color: object = pygame.Color(0)

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

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)
                # [(475, 199), (293, 192)]
                print('points', points)
                speeds.append((random.random() * 2,
                               random.random() * 2))
                print('speeds', speeds)
                # [(1.3269306662523934, 0.0872619412459017)]

        gameDisplay.fill((0, 0, 0))
        # Increasing value continuously, but only in 360 degree
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        # <class 'pygame.Color' >
        # print(color, color.hsla)
        # (12, 0, 255, 255) (242.8235294117647, 100.0, 50.0, 100.0)

        draw_points(points)
        draw_points(get_knot(points, steps), "line", 3, color)

        if not pause:
            set_points(points, speeds)

        pygame.display.flip()

    # print("type(gameDisplay)", type(gameDisplay))
    # # <class 'pygame.Surface'>

    # print("gameDisplay.__dir__:  \n\t", gameDisplay.__dir__)
    # # <built-in method __dir__ of pygame.Surface object at 0x10c097ab0 >

    # print("gameDisplay.__doc__:  \n\t", gameDisplay.__doc__)
    # # Surface((width, height), flags=0, depth=0, masks=None) -> Surface
    # # Surface((width, height), flags=0, Surface) -> Surface
    # # pygame object for representing images

    # print("gameDisplay.__class:__\n\t", gameDisplay.__class__)
    # # <class 'pygame.Surface'>

    pygame.display.quit()
    pygame.quit()
    exit(0)


def add(x, y):
    # сумма двух векторов
    return x[0] + y[0], x[1] + y[1]


def mul(v, k):
    # умножение вектора на число
    return v[0] * k, v[1] * k


def get_point(points: List[int, int], alpha, deg=None):
    # Сглаживание ломаной
    if deg is None:
        deg = len(points) - 1
    if deg == 0:
        return points[0]
    return add(mul(points[deg], alpha),
               mul(get_point(points, alpha, deg - 1),
                   1 - alpha))


def get_points(base_points, steps: int):
    alpha: float = 1 / steps
    res = []
    for i in range(steps):
        res.append(get_point(base_points, i * alpha))
    return res


def get_knot(points, steps):
    if len(points) < 3:
        return []
    res = []
    for i in range(-2, len(points) - 2):
        ptn = []
        ptn.append(mul(add(points[i], points[i + 1]), 0.5))
        ptn.append(points[i + 1])
        ptn.append(mul(add(points[i + 1],
                           points[i + 2]), 0.5))

        res.extend(get_points(ptn, steps))
    return res


def draw_points(points, style="points",
                width=3, color=(255, 255, 255)):
    # "Отрисовка" точек
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
