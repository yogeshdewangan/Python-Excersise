class A:
    def fun(self):
        print("fun is called")

def fun(self):
    print("monkey patched function")
A.fun= fun
a = A()
a.fun()

# Monkey patching is to bind the new function to existing class
# Python classes are mutable and methods are just attributes
# The most common usecase is adding a workaround for a bug in a module(or third party module) or class when you cannot change the original code