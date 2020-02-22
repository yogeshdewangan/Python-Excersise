# instance variable values will be different for each instances
# instance variables are defined and decleard inside constructor

class Shark:
    def __init__(self, name, age):
        self.name=name  #instance variable
        self.age = age  #instance variable

    def get(self):
        self.area= "sea"   # not instance variable. variable decleard and defined in method block will not be accessible via object

shark =Shark("sdf","sdf")
print(shark.name)
print(shark.area)  # Will not work "Shark object has no attribute 'area'"

