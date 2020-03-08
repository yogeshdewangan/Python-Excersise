t1 = ('a', 'b', 'c', 'd', 'e', 'f')
t2 = (1, 2, 3, 4)

print(zip(t1, t2))

A0 = dict(zip(t1, t2))
print("A0: " + str(A0))

A1 = range(10)
print("A1: " + str(A1))

A2 = sorted([i for i in A1 if i in A0])
print("A2: " + str(A2))

A3= sorted([A0[s] for s in A0] )
print("A3: " + str(A3))

A4= [i for i in A1 if i in A3]
print("A4: " + str(A4))

A5 = {i:i*i for i in A1}
print("A5: " + str(A5))

A6 = [[i, i*i] for i in A1]
print("A6: " + str(A6))
