list = [25,4,6,7,8,2,3,4,1,9]

print(min(list))

# Another way
smallest = list[0]
for i in list:
    if smallest> i:
        smallest = i
print(smallest)

# Another way
list1= sorted(list)
print(list1[0])

# Another way
list.sort()
print(list[0])


