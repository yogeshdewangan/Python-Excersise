
class Shark:
    anymal_type = "Fish"
    location = "Sea"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_followers(self, followers):
        from locale import str
        print("This user has " + str(followers) + " followers")


sammy = Shark("Sammy", 5)

# Print out instance variable name
print(sammy.name)

# Print out class variable location
print(sammy.location)

# Second object
stevie = Shark("Stevie", 8)

# Print out instance variable name
print(stevie.name)

# Use set_followers method and pass followers instance variable
stevie.set_followers(77)

# Print out class variable animal_type
print(stevie.anymal_type)