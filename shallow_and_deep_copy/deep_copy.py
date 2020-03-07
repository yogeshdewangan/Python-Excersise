
# any modification on any part of object wont reflect on original one
import copy

l3= [[1,2],[3,4], 5]

l4= copy.deepcopy(l3)

l4[1].append(6)
l4.append(7)

print("L3: " + str(l3))
print("L4: " + str(l4))