mylist = [1, 1, 2, 3, 4, 5, 6]
mylist = list(dict.fromkeys(mylist))
print(mylist)

mylist = [1, 1, 2, 3, 4, 5, 6]
mylist= list(set(mylist))

print(mylist)

mylist = [1, 1, 2, 3, 4, 5, 6]

count =0
final_list = []
for i in mylist:
    if i not in final_list:
        final_list.append(i)

print(final_list)



