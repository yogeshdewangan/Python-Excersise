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


def normalize(in_str):
    return "".join(
        filter(
            lambda x: x.lower() in "abcdefghijklmnopqrstuvwxyz",
            in_str)
    ).lower()


for my_string in palendromes:

    # temp_string = my_string.replace('!','').replace('.','').replace(',','').replace('-','').replace(' ','').replace("'"."").replace('?','').lower()
    temp_string = normalize(my_string)

    length = len(temp_string)
    # half = int(length/2)

    # first_half = temp_string[:half]
    # second_half = temp_string[half:]

    second_half_rev = ''.join(reversed(temp_string))

    if temp_string != second_half_rev:
        print(temp_string)

