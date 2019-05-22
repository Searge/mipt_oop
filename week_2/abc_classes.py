from abc import ABC, abstractmethod


class A:
    @abstractmethod
    def do_somethig(self):
        print('Hi!')


a = A()

a.do_somethig()


class B(ABC):
    @abstractmethod
    def do_somethig(self):
        print('Hi!')


b = B()
b.do_somethig()
# TypeError: Can't instantiate abstract class B
# with abstract methods do_somethig
