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


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)]
                                for _ in range(20)]
        self.map[5][7] = 1  # Источники света
        self.map[5][2] = -1  # Стены

    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(dim)


if __name__ == '__main__':
    system = System()
    lights = Light((0, 0))
    adapter = MappingAdapter(lights)
    system.get_lightening(adapter)
