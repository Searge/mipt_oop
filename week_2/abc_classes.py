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


# b = B()
# b.do_somethig()
# TypeError: Can't instantiate abstract class B
# with abstract methods do_somethig

class C(B):
    def do_something_else(self):
        print("Hello")


# c = C()
# c.do_something_else()
# TypeError: Can't instantiate abstract class C
# with abstract methods do_somethig


class D(B):
    def do_somethig(self):
        print('Hi 2!')


d = D()
d.do_somethig()
