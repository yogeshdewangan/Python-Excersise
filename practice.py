import sys

# Selection sort
# list = [6, 3, 4, 2, 1, 8, 9]

list = [6, 3, 4, 2, 1, 8, 9]

for i in range(len(list)):
    smallest =i
    for j in range(i+1, len(list)):
        if list[j]< list[smallest]:
            smallest =j
    list[i], list[smallest]= list[smallest], list[i]

print list

# Insertion sort
"""
list = [7, 6, 5, 4, 3, 2]

for i in range(1, len(list)):
    key = list[i]
    j = i -1
    while j >=0 and key< list[j]:
        list[j+1]= list[j]
        j -=1
    list[j+1] = key


print(list)

"""

# Bubble sort

"""
Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.


list = [5, 4, 3, 2, 1, -3]
count = 0
for i in range(len(list)):
    swapped = False
    for j in range(len(list) - i - 1):
        if list[j + 1] < list[j]:
            list[j + 1], list[j] = list[j], list[j + 1]
            swapped = True
        count += 1
    if not swapped:
        break;
    count += 1
print list
print count

"""
