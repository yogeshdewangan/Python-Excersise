
def generator_fun(n):

    number = 0
    while number< 20:
        yield number
        number += 1


g=  generator_fun(22)

print (next(g))

print (next(g))
print (next(g))
print (next(g))