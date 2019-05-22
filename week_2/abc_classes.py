from abc import ABC, abstractmethod


class A:
    @abstractmethod
    def do_somethig(self):
        print('Hi!')


a = A()

a.do_somethig()
