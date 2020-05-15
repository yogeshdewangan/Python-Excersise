list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 1]

list1_start = 0
list2_start = 0
identical = True

if len(list1) != len(list2):
    print "Not identical"

# find the index of first element of list1 in list2
for i in range(len(list2)):
    if list1[list1_start] == list2[i]:
        list2_start = i
        break

while list1_start < len(list1):

    if list2_start >= len(list2):
        list2_start = list2_start % len(list2)

    if list1[list1_start]!= list2[list2_start]:
        identical = False

    list1_start += 1
    list2_start += 1

print identical


# Another way
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 1]

s= ''.join(map(str, list1))
s1= ''.join(map(str, list2 *2))

if ''.join(map(str, list1)) in ''.join(map(str, list2 *2)):
    print "identical"
else:
    print "not identical"

