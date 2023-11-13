

"""
Write a Python program to generate all permutations of a list in Python
"""
"""
In mathematics, the notion of permutation relates to the act of arranging all the members of a set into some sequence or order, 
or if the set is already ordered, rearranging (reordering) its elements, a process called permuting. These differ from combinations, 
which are selections of some members of a set where order is disregarded
"""

lst =[1,2,3,4]

import itertools

print (len(list(itertools.permutations(lst))))
print (list(itertools.permutations(lst)))



# Another way



ini_str = "abc"

# Printing initial string
print("Initial string", ini_str)

# Finding all permuatation
result = []

def permute(data, i, length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]

permute(list(ini_str), 0, len(ini_str))
# Printing result
print("Resultant permutations", str(result))