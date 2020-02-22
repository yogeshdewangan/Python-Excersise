
class Example:
    var1 = 1
    def __init__(self, name):
        self.name = name

    def instance_method(self):
        self.age =20
        print("age is : "+ str(self.age))


    @staticmethod
    def static_method():
        print("static method dont have self as first parameter, and cannot access class and instance variables. Can be used as utility function")
        var2= 100

    @classmethod
    def class_method(cls):
        print("Class methods can access only class variables")
        #print("Instance variable accessibility: "+ cls.name)     # class method should not call any of the instance variable, only class variable is accessible
        print("Class variable accessibility: " + str(cls.var1))
        cls.var3=200


example = Example("Yogesh")
example.instance_method()
print(example.age)   # instance variable can be accessed using object
print(example.var1)  # class variable also can be accessed using object

#Example.instance_method()  # instance method cannot be called using Class name
Example.static_method()
Example.class_method()  # class methods can be called directly by class name, and by object as well
example.class_method()

#print(example.var2) # not accessible because var2 is declared in static method
#print(example.var3) # not accessible because var3 life is inside class_method only


