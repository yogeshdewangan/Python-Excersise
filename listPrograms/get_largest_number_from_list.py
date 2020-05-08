list1 = [25,4,6,7,8,2,3,4,1,9]

largest=list1[0]
for i in list1:
    if i>largest:
        largest = i

print(largest)



# Another way

list1.sort()
print(list1[len(list1)-1])


# Another way

print(max(list1))
