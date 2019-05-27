# Реализуем адаптер для класса
class MappingAdapter:

    def __init__(self, adaptee):
        # Сохраним адаптируемый объект
        self.adaptee = adaptee

    def lighten(self, grid):
        # Определим метод рассчета освещенности
        dim = (len(grid[0]), len(grid))  # Определение размера карты
        self.adaptee.set_dim(dim)  # Установка размера карты в адаптируемом объекте
        # Инициализируем пустые списки препятствий и источников света
        obst = []
        lght = []
        # Считаем положения объектов с исходной карты
        for i in range(dim[0]):
            for j in range(dim[1]):
                if grid[j][i] == 1:
                    lght.append((i, j))
                elif grid[j][i] == -1:
                    obst.append((i, j))
        # Передадим положения объектов адаптируемому объекту
        self.adaptee.set_lights(lght)
        self.adaptee.set_obstacles(obst)
        # Вернем полученную карту освещенности
        return self.adaptee.grid
