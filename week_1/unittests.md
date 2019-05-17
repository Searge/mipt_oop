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

```shell
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

Заметим, что assertEqual(a, b) для строк, последовательностей, списков, кортежей, множеств и словарей осуществляет [специализированную по типу проверку](https://docs.python.org/3/library/unittest.html#type-specific-methods).

Есть также проверки, проводящие сравнение и проверки включения:

|        Вариант assert        |                    Что проверяет                    |
| :--------------------------: | :-------------------------------------------------: |
|  `assertAlmostEqual(a, b)`   |                `round(a-b, 7) == 0`                 |
| `assertNotAlmostEqual(a, b)` |                `round(a-b, 7) != 0`                 |
|    `assertGreater(a, b)`     |                       `a > b`                       |
|  `assertGreaterEqual(a, b)`  |                      `a >= b`                       |
|      `assertLess(a, b)`      |                       `a < b`                       |
|   `assertLessEqual(a, b)`    |                      `a <= b`                       |
|     `assertRegex(s, r)`      |                    `r.search(s)`                    |
|    `assertNotRegex(s, r)`    |                  `not r.search(s)`                  |
|   `assertCountEqual(a, b)`   | `контейнеры равны с точностью до порядка элементов` |

### Выделение подслучая

Для выделения конкретной ситуации, в рамках которой произошла ошибка, удобно использовать метод self.subTest():

```python
class TestSort(unittest.TestCase):
    def test_simple_cases(self):
        cases = ([1], [], [1, 2], [1, 2, 3, 4, 5],
                 [4, 2, 5, 1, 3], [5, 4, 4, 5, 5],
                 list(range(1, 10)), list(range(9, 0, -1)))
        for b in cases:
            with self.subTest(case=b):
                a = list(b)
                sort_algorithm(a)
                self.assertCountEqual(a, b)
                self.assertTrue(is_not_in_descending_order(a))

```

В этом случае тестирование не остановится на первой же ошибке в рамках метода test_simple_cases(), но продолжится для других случаев. А содержание ошибки из-за передачи параметра (case=b) становится информативнее:

```shell
======================================================================
FAIL: test_simple_cases (__main__.TestSort) (case=[4, 2, 5, 1, 3])
----------------------------------------------------------------------
Traceback (most recent call last):
  File "unittest_sort_n2_2.py", line 35, in test_simple_cases
    self.assertTrue(is_not_in_descending_order(a))
AssertionError: False is not true

======================================================================
FAIL: test_simple_cases (__main__.TestSort) (case=[5, 4, 4, 5, 5])
----------------------------------------------------------------------
Traceback (most recent call last):
  File "unittest_sort_n2_2.py", line 35, in test_simple_cases
    self.assertTrue(is_not_in_descending_order(a))
AssertionError: False is not true

======================================================================
FAIL: test_simple_cases (__main__.TestSort) (case=[9, 8, 7, 6, 5, 4, 3, 2, 1])
----------------------------------------------------------------------
Traceback (most recent call last):
  File "unittest_sort_n2_2.py", line 35, in test_simple_cases
    self.assertTrue(is_not_in_descending_order(a))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=3)

```

Для повышения информативности отчёта можно также использовать именованный параметр msg этих методов:

```python
self.assertCountEqual(a, b, msg="Elements changed. a = "+str(a))
self.assertTrue(is_not_in_descending_order(a),
                msg="List not sorted. a = "+str(a))
```

### Тестирование возбуждения исключений

Хороший программный код должен быть устойчивым в тех случаях, когда его используют с некорректными параметрами. В частности, метод или функция должны возбуждать определённое исключение, когда возникает конкретная внештатная ситуация.

```python
self.assertRaises(ValueError, math.sqrt, -1)
```

Обратите внимание, что при использовании assertRaises нельзя вызывать функцию. Мы передаём ему ссылку на функцию и её параметры, чтобы она была вызвана уже внутри метода assertRaises, описанного в библиотеке unittest.

Если тестируемая функция не вызывает ожидаемого исключения, это считается ошибкой:

```shell
======================================================================
FAIL: test_simple_cases (__main__.TestSort) (case=[4, 2, 5, 1, 3])
----------------------------------------------------------------------
Traceback (most recent call last):
  File "unittest_sort_n2_2.py", line 35, in test_simple_cases
    self.assertTrue(is_not_in_descending_order(a))
AssertionError: False is not true

======================================================================
FAIL: test_simple_cases (__main__.TestSort) (case=[5, 4, 4, 5, 5])
----------------------------------------------------------------------
Traceback (most recent call last):
  File "unittest_sort_n2_2.py", line 35, in test_simple_cases
    self.assertTrue(is_not_in_descending_order(a))
AssertionError: False is not true

======================================================================
FAIL: test_simple_cases (__main__.TestSort) (case=[9, 8, 7, 6, 5, 4, 3, 2, 1])
----------------------------------------------------------------------
Traceback (most recent call last):
  File "unittest_sort_n2_2.py", line 35, in test_simple_cases
    self.assertTrue(is_not_in_descending_order(a))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=3)

```

Для повышения информативности отчёта можно также использовать именованный параметр msg этих методов:

```python
self.assertCountEqual(a, b, msg="Elements changed. a = "+str(a))
self.assertTrue(is_not_in_descending_order(a),
                msg="List not sorted. a = "+str(a))
```