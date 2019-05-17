# Использование unittest

## Инструментарий библиотеки:

1. `Test case` — тестовый случай, базовая единица тестирования.
2. `Test fixture` — среда исполнения теста. Включает подготовку к тестированию и последующее обнуление данных, используемых в тестовом случае.
3. `Test suite` — набор тестовых случаев.
4. `Test runner` — группа запуска тестов. Это множество классов, связанных с запуском и представлением тестов.

## Тестовый случай (test case)

Для начала самое главное — научиться создавать тестовые случаи ("тест-кейсы"):

```python
class MyTest(unittest.TestCase):
    def test_usage(self):
        self.assertEqual(2+2, 4)

```

Обратите внимание, что:

1. класс тестового случая — потомок unittest.TestCase;
2. тестирующий метод начинается со слова «test»;
3. для проверки утверждения используется метод self.assertEqual().

Если не соблюдать эти правила, то ваш метод либо не будет выполнен, либо ошибка не будет корректно обработана.

### Пример тестового случая

Оформим тестирование сортировки методом пузырька в тестовый случай unittest. При этом воспользуемся сравнением assertCountEqual(a, b) и проверкой упорядоченности списка a за один проход по нему.

```python
import unittest


def sort_algorithm(A: list):
    pass  # FIXME


def is_not_in_descending_order(a):
    """
    Check if the list a is not descending (means "rather ascending")
    """
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True


class TestSort(unittest.TestCase):
    def test_simple_cases(self):
        cases = ([1], [], [1, 2], [1, 2, 3, 4, 5],
                 [4, 2, 5, 1, 3], [5, 4, 4, 5, 5],
                 list(range(10)), list(range(10, 0, -1)))
        for b in cases:
            a = list(b)
            sort_algorithm(a)
            self.assertCountEqual(a, b)
            self.assertTrue(is_not_in_descending_order(a))


if True: #__name__ == "__main__":
    unittest.main()
```

```console
test_simple_cases (submission.TestSort) ... FAIL

======================================================================
FAIL: test_simple_cases (submission.TestSort)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/tmp/ggalh/submission.py", line 40, in test_simple_cases
    self.assertTrue(is_not_in_descending_order(a))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
```

Запуск данного теста конечно покажет нам ошибку, но не будет ясно, при каком конкретно случае она случилась.

Запустите интерактивный код выше и посмотрите на ошибку. Можете написать свою версию сортировки и посмотреть на результаты тестирования.

Обратите внимание на вызов unittest.main(), которая запускает все тесты из данного модуля. В данном случае она запускается всегда (if True), чтобы вы могли посмотреть код в интерактивном режиме.


|       Вариант assert        |     Что проверяет      |
| :-------------------------: | :--------------------: |
|     `assertEqual(a, b)`     |        `a == b`        |
|   `assertNotEqual(a, b)`    |        `a != b`        |
|       `assertTrue(x)`       |   `bool(x) is True`    |
|      `assertFalse(x)`       |   `bool(x) is False`   |
|      `assertIs(a, b)`       |        `a is b`        |
|     `assertIsNot(a, b)`     |      `a is not b`      |
|      `assertIsNone(x)`      |      `x is None`       |
|    `assertIsNotNone(x)`     |    `x is not None`     |
|      `assertIn(a, b)`       |        `a in b`        |
|     `assertNotIn(a, b)`     |      `a not in b`      |
|  `assertIsInstance(a, b)`   |   `isinstance(a, b)`   |
| `assertNotIsInstance(a, b)` | `not isinstance(a, b)` |

