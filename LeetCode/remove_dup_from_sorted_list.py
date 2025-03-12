my_list = [1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8]

my_dict = {}

for i in my_list:
    if i in my_dict.keys():
        my_dict[i] += 1
    else:
        my_dict[i] = 1

new_list = []
for key, value in my_dict.items():
        new_list.append(key)

print(new_list)

