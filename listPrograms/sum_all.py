list= [1,2,3,4,5]

sum_total =0
for i in list:
    sum_total+=i
print(sum_total)

# Another way
print(sum(list))

# Anather way
print(sum(i for i in list))

# Find the average
print(sum(i for i in list)/len(list))


# Anather way to add some number in the result, sum takes two arguments
print(sum((i for i in list), 30))



