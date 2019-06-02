class Light:
    """
    Рассчёт освещенности на карте
    """

    def __init__(self, dim):
        """
        Создаем поле заданного размера:
        :type dim: Tuple[int, int]
            - width, height = dim[0], dim[1]
        """
        self.dim = dim
        # n-мерный масив нулей
        self.grid = [[0 for i in range(dim[0])]
                     for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []

    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])]
                     for _ in range(dim[1])]

    def set_lights(self, lights):
        """
        устанавливает массив источников света с заданными координатами
        и просчитывает освещение
        """
        self.lights = lights
        self.generate_lights()

    def set_obstacles(self, obstacles):
        """
        устанавливает препятствия аналогичным образом
        """
        self.obstacles = obstacles
        self.generate_lights()

    def generate_lights(self):
        return self.grid.copy()


class MappingAdapter:
    def __init__(self, adaptee):
        pass

    def lighten(self, grid):
        pass
