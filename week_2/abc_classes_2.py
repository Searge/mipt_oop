from abc import ABC, abstractmethod


class A(ABC):
    def __init__(self):
        self.var1 = 5
        self.var2 = 7

    @abstractmethod
    def do_something(self):
        print(self.var1 + self.var2)


class B(A):
    def __init__(self):
        self.var1 = 2


obj = B()
obj.do_something()
