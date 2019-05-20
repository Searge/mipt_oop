# SOLID-принципы
## Принцип единственной ответственности (The Single Responsibility Principle)

У каждого объекта должна быть только одна ответственность. Все поведение этого объекта должно быть направлено на обеспечение этой ответственности и никаких других.

```python
# Неправильно
class EventHandler: # Обработчик событий
    def handle_event_1(self, event):
        # Обработчик первого события
        pass

    def handle_event_2(self, event):
        # Обработчик второго события
        pass

    def handle_event_3(self, event):
        # Обработчик третьего события
        pass

    def database_logger(self, event):
        # Метод для записи логов в базу данных
        pass


# Правильно
class  EventHandler: # Обработчик событий

    def handle_event_1(self, event):
        # Обработчик первого события
        pass

    def handle_event_2(self, event):
        # Обработчик второго события
        pass

    def handle_event_3(self, event):
        # Обработчик третьего события
        pass


class DatabaseLogger:

    def database_logger(self, event):
        # Метод для записи логов в базу данных
        pass

```

## Принцип открытости/закрытости (The Open Closed Principle)

Классы должны быть открыты для расширения, но закрыты для изменения. Этот принцип является важным, потому что внесение изменений в существующие компоненты системы может также привести к непредвиденным изменения в работе самой этой системы. Однако поведение существующих объектов при необходимости можно расширить при помощи создания новых сущностей.

Рассмотрим на примере. Пусть существует класс `Robot`. У этого класса есть метод `brake`. Мы хотим создать робота, который при поломке кроме всего прочего включает аварийную сигнализацию `alarm`. При этом мы не должны переписывать сам класс `Robot`, а должны создать потомка `AlarmRobot`, который при вызове break после вызова соответствующего метода родительского класса будет так же вызывать метод `alarm`.

## Принцип подстановки Барбары Лисков (The Liskov Substitution Principle)

Функции, которые используют базовый тип должны иметь возможность использовать его подтипы не зная об этом.

```python
# Неправильный код
class Parent:
    def __init__(self, value):
        self.value = value

    def do_something(self):
        print("Function was called")


class Child(Parent):

    def do_something(self):
        super().do_something()
        self.value = 0


def function(obj: Parent):
    obj.do_something()
    if obj.value > 0:
        print("All correct!")
    else:
        print("SOMETHING IS GOING WRONG!")

# Посмотрим на поведение
parent = Parent(5)
function(parent)
print()

# Данный код должен работать корректно, если вместо родителя подставить потомка
child = Child(5)
function(child)
print()
```

## Принцип разделения интерфейса (The Interface Segregation Principle)
Клиенты не должны зависеть от методов, которые они не используют.

```python
# Неправильно
class AllScoresCalculator:
    def calculate_accuracy(self, y_true, y_pred):
        return sum(int(x == y) for x, y in zip(y_true, y_pred)) / len(y_true)

    def log_loss(self, y_true, y_pred):
        return sum((x * math.log(y) + (1 - x) * math.log(1 - y))
                   for x, y in zip(y_true, y_pred)) / len(y_true)


# Правильно
class CalculateLosses:
    def log_loss(self, y_true, y_pred):
        return sum((x * math.log(y) + (1 - x) * math.log(1 - y))
                   for x, y in zip(y_true, y_pred)) / len(y_true)


class CalculateMetrics:
    def calculate_accuracy(self, y_true, y_pred):
        return sum(int(x == y) for x, y in zip(y_true, y_pred)) / len(y_true)

```

## Принцип инверсии зависимостей (The Dependency Inversion Principle):

- Модули верхних уровней не должны зависеть от модулей нижних уровней.
  - Оба типа модулей должны зависеть от абстракций.
- Абстракции не должны зависеть от деталей.
  - Детали должны зависеть от абстракций.

Приведем пример. Пусть у вас есть базовый класс `Distributer`, который может отправлять сообщения в различные социальные сети. У этого класса есть несколько реализаций, например `VKDistributer` и `OKDistributer`. Согласно принципу инверсии зависимостей, эти реализации не должны зависеть от методов класса `Distributer` (например `VK_send_message` и `OK_send_message`). Вместо этого у класса `Destributor` должен быть объявлен общий абстрактный метод `send_message`, который и будет реализован отдельно в каждом из потомков.

