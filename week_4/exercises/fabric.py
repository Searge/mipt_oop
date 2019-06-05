import random


class AbstractLevel:
    class Map:
        pass

    class Object:
        pass

    @classmethod
    def get_map(cls):
        return cls.Map()

    @classmethod
    def get_objects(cls):
        return cls.Object()


class EasyLevel(AbstractLevel):
    class Map:
        def __init__(self):
            self._map = [[0 for j in range(5)] for i in range(5)]
            for i in range(5):
                for j in range(5):
                    if i == 0 or j == 0 or i == 4 or j == 4:
                        # граница карты
                        self._map[j][i] = -1
                    else:
                        # случайная характеристика области
                        self._map[j][i] = random.randint(0, 2)

        def get_map(self):
            return self._map

    class Object:
        def __init__(self):
            # размещаем переход на след. уровень
            self.objects = [('next_lvl', (2, 2))]

        def get_objects(self, map_obj):
            # размещаем противников
            for obj_name in ['rat']:
                coord = (random.randint(1, 3), random.randint(1, 3))
                # ищем случайную свободную локацию
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 3), random.randint(1, 3))

                self.objects.append((obj_name, coord))

            return self.objects
