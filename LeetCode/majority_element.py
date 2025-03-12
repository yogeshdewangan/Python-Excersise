my_list = [1, 1, 2, 3, 3, 2, 5, 5, 2, 7, 5,5,5,5,8, 8]
my_dict = {}

for i in my_list:
    if i in my_dict.keys():
        my_dict[i] += 1
    else:
        my_dict[i] = 1

max_value_key = max(zip(my_dict.values(), my_dict.keys()))[1]
print(max_value_key)

#  or

max_value_key = max(my_dict, key= lambda x: my_dict[x])