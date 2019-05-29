from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):
    def feed(self):
        print("I eat grass")

    def move(self):
        print("I walk forward")

    def make_noise(self):
        print("WOOO!")


class AbstractDecorator(Creature):
    def __init__(self, obj):
        """
        Сохраняем базовый объект для нашего декоратора в переменную
        """
        self.obj = obj

    def feed(self):
        self.obj.feed()

    def move(self):
        self.obj.move()

    def make_noise(self):
        self.obj.make_noise()


class Swimming(AbstractDecorator):
    def move(self):
        print("I swim")

    def make_noise(self):
        print("...")


class Predator(AbstractDecorator):
    def feed(self):
        print("I eat other animals")


class Fast(AbstractDecorator):
    def move(self):
        self.obj.move()
        print("Fast!")


if __name__ == "__main__":
    # Создадим базовое животное и выполним все его методы:
    animal = Animal()
    print(animal)
    animal.feed()
    animal.move()
    animal.make_noise()

    # Теперь сделаем из нашего животного водоплавающее.
    # Для этого определим, что оно является водоплавающим и
    # в качестве декорируемого объекта укажем наше животное.
    swimming = Swimming(animal)
    print(swimming)
    swimming.feed()
    swimming.move()
    swimming.make_noise()

    # Оно ест траву, плавает и не издаёт звуков.
    # Сделаем из нашего животного хищника:
    predator = Predator(animal)
    print(predator)
    predator.feed()
    predator.move()
    predator.make_noise()

    # Получили быстрого водоплавающего хищника.
    fast = Fast(animal)
    print(fast)
    fast.feed()
    fast.move()
    fast.make_noise()

    # можно применять несколько одинаковых декораторов к одному объекту.
    # Мы можем сделать наше животное ещё быстрее:
    faster = Fast(fast)
    print(faster)
    faster.feed()
    faster.move()
    faster.make_noise()

    # Base object w/o Decoratar
    print(faster.obj.obj)
