
def generator_fun():

    number = 0
    while number< 20:
        yield number
        number += 1


g=  generator_fun()

print (next(g))

print (next(g))
print (next(g))
print (next(g))