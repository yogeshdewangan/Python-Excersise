
"""
Write a Python program to find the list of words that are longer than n from a given list of words
"""


list= ["Yogesh", "is", "my", "love"]
n=3
new_list=[]
for item in list:
    if len(item)>3:
        new_list.append(item)

print new_list


"""
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

# Another way
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new_color=[]
for (i,x) in enumerate(color):
    if i not in (0,4,5):
        new_color.append(x)
print new_color

"""
Write a Python program to print the numbers of a specified list after removing even numbers from it
"""

list=[1,2,3,4,5,6,7,8]

list =[x for x in list if not x%2==0]

print list

"""
Write a Python program to shuffle and print a specified list
"""
from random import shuffle
lst=[1,2,3,4,5,6,7,8]
shuffle(lst)
print lst

