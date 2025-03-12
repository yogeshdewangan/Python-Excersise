#  right rotate

my_list = [1, 2, 3, 4, 5, 6]
k = 2
new_list = my_list[len(my_list)-k:] + my_list[:len(my_list)-k]
print(new_list)


#  Left rotate
my_list = [1, 2, 3, 4, 5, 6]
k = 5
new_list =  my_list[k:len(my_list)] + my_list[:k]
print(new_list)
