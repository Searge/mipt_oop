from modules import graphics as gr


def main():
    window = gr.GraphWin("My Image", 600, 600)
    # здесь должно быть содержимое
    draw_image(window)
    window.getMouse()


def draw_image(window):
    house_x, house_y = window.width // 2, window.height * 2 // 3
    house_width = window.width // 3
    house_height = house_width * 4 // 3

    draw_background(window)
    draw_house(window, house_x, house_y,
               house_width, house_height)


def draw_background(window):
    earth = gr.Rectangle(gr.Point(0, window.height // 2),
                         gr.Point(window.width - 1, window.height - 1))
    earth.setFill("green")
    earth.draw(window)
    sci = gr.Rectangle(gr.Point(0, 0),
                       gr.Point(window.width - 1, window.height // 2))
    sci.setFill("cyan")
    sci.draw(window)


def draw_house(window, x, y, width, height):
    foundation_height = height // 8
    walls_height = height // 2
    walls_width = 7 * width // 8
    roof_height = height - walls_height - \
        foundation_height
    draw_house_foundation(window, x, y, width, foundation_height)
    draw_house_walls(window, x, y - foundation_height,
                     walls_width, walls_height)
    draw_house_roof(window, x,
                    y - foundation_height - walls_height,
                    width, roof_height)

# обязательно создаём функции-заглушки перед переключением


def draw_house_foundation(window, x, y, width, height):
    foundation = gr.Rectangle(gr.Point(x - width // 2, y),
                              gr.Point(x + width // 2,
                                       y - height))
    foundation.setFill("brown")
    foundation.draw(window)


def draw_house_walls(window, x, y, width, height):
    walls = gr.Rectangle(gr.Point(x - width // 2, y),
                         gr.Point(x + width // 2, y - height))
    walls.setFill("red")
    walls.draw(window)
    draw_house_window(window, x, y - height // 4,
                      width // 3, height // 2)


def draw_house_window(window, x, y, width, height):
    glass = gr.Rectangle(gr.Point(x - width // 2, y),
                         gr.Point(x + width // 2, y - height))
    glass.setFill("blue")
    line1 = gr.Line(gr.Point(x, y),
                    gr.Point(x, y - height))
    line2 = gr.Line(gr.Point(x - width // 2,
                             y - height // 2),
                    gr.Point(x + width // 2,
                             y - height // 2))
    glass.draw(window)
    line1.draw(window)
    line2.draw(window)
    line1.setOutline("black")
    line2.setOutline("black")
    line1.setWidth(2)
    line2.setWidth(2)


def draw_house_roof(window, x, y, width, height):
    roof = gr.Polygon(gr.Point(x - width // 2, y),
                      gr.Point(x + width // 2, y),
                      gr.Point(x, y - height))

    roof.setFill("green")
    roof.draw(window)


if __name__ == "__main__":
    main()

"""
## Замечание автора

Этот программный код нельзя назвать образцовым.
Дело в том, что в функциях отсутствуют документ-строки,
а документирование функций — это очень важно.
Однако, в данном уроке нет цели обучить этому навыку.
В ущерб перфекционизму мы здесь концентрируемся на парадигме
структурного программирования, а особенно на навыке декомпозиции задачи
и итеративном движении сверху-вниз.
"""
