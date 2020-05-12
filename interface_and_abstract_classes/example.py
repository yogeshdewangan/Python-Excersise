
from abc import ABCMeta, abstractmethod


class A(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def method1(self, name):
        ...

    def method2(self):
        print("method2")

class B(A):

    def method3(self):
        self.method2()

    def method1(self, name):
        print("abstract method1")

b = B()
b.method3()
b.method1("yogesh")