import copy

#Copy via assignment
#only reference will be copied to new instance. Any modification in new one will reflect on other one
#Memory location is same for both the instances
print("Assignment copy ----------")

l1 = [1,2,3,4]

print("L1: " + str(l1))
print("Memory Location L1: "+ str(id(l1)) )

l2= l1          # will have same memory location

print("L2: " + str(l2))
print("Memory Location L3: "+ str(id(l2)) )

print("adding a new value in L2")
l2.append(5)

print("L1: " + str(l1))
print("L2: " + str(l2))



