# anti clock rotation
list = [3, 2, 5, 1, 8, 7]

rotation =13
for j in range(rotation):
    temp = list[0]

    for i in range(len(list)):
        if i+1 ==len(list):
            list[i] = temp
            break
        list[i]= list[i+1]
print (list)


#================================================================
# clock wise rotation
list1 = [3, 2, 5, 1, 8, 7]

rotation = 3
print ("oritinal list"+ str(list1))

for j in range(rotation):
    temp = list1[len(list1)-1]

    for i in range(len(list1)-1, 0, -1):

        list1[i]= list1[i-1]
    list1[0]=temp

print (list1)









