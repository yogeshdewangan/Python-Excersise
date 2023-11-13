list = [5, 1, -96, -4, 2, 3, -1, -8, 9]

first_smallest = list[0]
second_smallest = list[0]


for i in range(1, len(list)):
    if first_smallest > list[i] :
        first_smallest = list[i]

list.remove(first_smallest)

for i in range(1, len(list)):
    if second_smallest > list[i] :
        second_smallest = list[i]


print (second_smallest)


