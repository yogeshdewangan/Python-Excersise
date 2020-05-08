mylist = [1, 1, 2, 3, 4, 5, 6]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# Another way

mylist = [1, 1, 2, 3, 4, 5, 6]
mylist= list(set(mylist))

print(mylist)

# Another way

mylist = [1, 1, 2, 3, 4, 5, 6, 'ewr','ewr']

count =0
final_list = []
for i in mylist:
    if i not in final_list:
        final_list.append(i)

print(final_list)

# Check if list is empty or not
list=[1]
list1=[]
print(len(list)==0)
print(not list)



