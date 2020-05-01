
#CLASS VARIABLES
#When we want variable to be consistent to all instances of class, we make it class variable
#And this class variable's value is shared accross all instances of the class
#its a static variable, if any class instance changes its value, it will reflect to all other instances

#INSTANCE VARIABLES
#


class Shark:
    animal_type="Fish"

shark= Shark()
print(shark.animal_type)
#As animal_type is class variable and internally its static, we can use it with Class name
print(Shark.animal_type)

shark1= Shark()
#Change the value, new object will have sea fish value as its static variable and can be changed, And it will refect to all object of the class
Shark.animal_type="Sea Fish"

print(shark1.animal_type)

