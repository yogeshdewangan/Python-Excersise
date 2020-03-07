
import copy

#Shallow copy
#In shallow copy new instance will be created with new memory location
#Any modification in new one wont reflect on new one, but any modication in inside object (e.g. list of lists) will reflect on original one
print("Shallow copy ----------")

l1 = [1,2,3,4]

print("L1: " + str(l1))
print("Memory Location L1: "+ str(id(l1)) )

l2= copy.copy(l1)         #Shallow copy  l2=l1[:] another way to do shallow copy

print("L2: " + str(l2))
print("Memory Location L3: "+ str(id(l2)) )

print("adding a new value in L2")
l2.append(5)   # adding new value in l2 wont reflect on l1

print("L1: " + str(l1))
print("L2: " + str(l2))

# Now adding a new element in list inside l3. It will reflect on origin list l3
l3= [[1,2],[3,4], 5]

l4= copy.copy(l3)

l4[1].append(6)

print("L3: " + str(l3))
print("L4: " + str(l4))