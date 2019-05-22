from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def do_somethig(self):
        print('Hi!')


class B(A):
    def do_somethig(self):
        print('Hello!')


class C(B):
    def do_somethig(self):
        print("What's Up!")


class D(B, C):
    def do_somethig(self):
        print('Sup!')


class E(D):
    pass


print("D(B, C):\t", list(filter(lambda x: "__" not in x, dir(D))))
print("E(D):\t", list(filter(lambda x: "__" not in x, dir(E))))
