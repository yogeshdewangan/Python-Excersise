"""
python 3.6 new feature
"""

# A python class that acts like dict

class Vehical:
    kind = "car"

    def __init__(self, type, model):
        self.type= type
        self.model  = model

def from_dict(dict):
    instance = Vehical(None, None)
    instance.__dict__.update(dict)
    return instance

car = Vehical("SUV", "Huyndai")
print (car.__dict__)

class_state = car.__dict__.copy()

del car
car = Vehical("sdf","sdf")
car.__dict__.update(class_state)
print (car.__dict__)

del car
car = from_dict(class_state)
print (car.__dict__)


