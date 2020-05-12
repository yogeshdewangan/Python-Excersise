class MyClass:
    name ="Yogesh"

    def __init__(self, age):
        self.age = age

    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls.name
        #return 'class method called', cls.name, cls.age            # gives error because cls.age is not an class variable

    @staticmethod
    def staticmethod():
        return 'static method called',


print MyClass.name

#print MyClass.method()    # wont work, we cannot access instance method with class name

print MyClass.staticmethod()   # We can call static method with directly class name

myclass= MyClass(35)

print myclass.staticmethod(myclass)  # we can also call static method with class object


print MyClass.classmethod()
print myclass.classmethod()

"""
class methods can access only class variables
static methods cannot access any variable either class or instance, it acts like utility function
both, static and class methods can be called using a class objet and directly from class name
instance methods cannot be called by class name

"""


