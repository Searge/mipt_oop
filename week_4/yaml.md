# Парсинг YAML-файла

Вам необходимо модифицировать приложенный код так, чтобы два следующих кода были эквивалентны (приводили к одинаковому результату)

```python
Lebels = yaml.load('''levels:
  - !easy_level {}
  - !medium_level
    enemy: ['rat']
  - !hard_level
    enemy: [
    - rat
    - snake
    - dragon
    enemy_count: 10''');
```

```python
Levels = {'levels':[]}
_map = EasyLevel.Map()
_obj = EasyLevel.Objects()
Levels['levels'].append({'map': _map, 'obj': _obj})

_map = MediumLevel.Map()
_obj = MediumLevel.Objects()
_obj.config = {'enemy':['rat']}
Levels['levels'].append({'map': _map, 'obj': _obj})

_map = HardLevel.Map()
_obj = Hard_Level.Objects()
_obj.config = {'enemy: ['rat', 'snake', 'dragon'], 'enemy_count': 10}
Levels['levels'].append({'map': _map, 'obj': _obj})

```

То есть в **Исходный код**:

```python
import random
import yaml
from abc import ABC


class AbstractLevel(yaml.YAMLObject):

    @classmethod
    def get_map(cls):
        return cls.Map()

    @classmethod
    def get_objects(cls):
        return cls.Objects()

    class Map(ABC):
        pass

    class Objects(ABC):
        pass


class EasyLevel(AbstractLevel):
    class Map:
        def __init__(self):
            self.Map = [[0 for _ in range(5)] for _ in range(5)]
            for i in range(5):
                for j in range(5):
                    if i == 0 or j == 0 or i == 4 or j == 4:
                        self.Map[j][i] = -1  # граница карты
                    else:
                        self.Map[j][i] = random.randint(0, 2)  # случайная характеристика области

        def get_map(self):
            return self.Map

    class Objects:
        def __init__(self):
            self.objects = [('next_lvl', (2, 2))]
            self.config = {}

        def get_objects(self, _map):
            for obj_name in ['rat']:
                coord = (random.randint(1, 3), random.randint(1, 3))
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 3), random.randint(1, 3))

                self.objects.append((obj_name, coord))

            return self.objects


class MediumLevel(AbstractLevel):
    class Map:
        def __init__(self):
            self.Map = [[0 for _ in range(8)] for _ in range(8)]
            for i in range(8):
                for j in range(8):
                    if i == 0 or j == 0 or i == 7 or j == 7:
                        self.Map[j][i] = -1  # граница карты
                    else:
                        self.Map[j][i] = random.randint(0, 2)  # случайная характеристика области

        def get_map(self):
            return self.Map

    class Objects:
        def __init__(self):
            self.objects = [('next_lvl', (4, 4))]
            self.config = {'enemy': []}

        def get_objects(self, _map):
            for obj_name in self.config['enemy']:
                coord = (random.randint(1, 6), random.randint(1, 6))
                intersect = True
                while intersect:
                    intersect = False
                    for obj in self.objects:
                        if coord == obj[1]:
                            intersect = True
                            coord = (random.randint(1, 6), random.randint(1, 6))

                self.objects.append((obj_name, coord))

            return self.objects


class HardLevel(AbstractLevel):
    class Map:
        def __init__(self):
            self.Map = [[0 for _ in range(10)] for _ in range(10)]
            for i in range(10):
                for j in range(10):
                    if i == 0 or j == 0 or i == 9 or j == 9:
                        self.Map[j][i] = -1  # граница карты :: непроходимый участок карты
                    else:
                        self.Map[j][i] = random.randint(-1, 8)  # случайная характеристика области

        def get_map(self):
            return self.Map

    class Objects:
        def __init__(self):
            self.objects = [('next_lvl', (5, 5))]
            self.config = {'enemy_count': 5, 'enemy': []}

        def get_objects(self, _map):
            for obj_name in self.config['enemy']:
                for tmp_int in range(self.config['enemy_count']):
                    coord = (random.randint(1, 8), random.randint(1, 8))
                    intersect = True
                    while intersect:
                        intersect = False
                        if _map[coord[0]][coord[1]] == -1:
                            intersect = True
                            coord = (random.randint(1, 8), random.randint(1, 8))
                            continue
                        for obj in self.objects:
                            if coord == obj[1]:
                                intersect = True
                                coord = (random.randint(1, 8), random.randint(1, 8))

                    self.objects.append((obj_name, coord))

            return self.objects

```