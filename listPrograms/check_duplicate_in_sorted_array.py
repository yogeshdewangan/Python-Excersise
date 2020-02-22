def check_duplicate_in_sorted_array(my_array):
    my_array.sort()
    for i in range(len(my_array) - 1):
        if my_array[i] == my_array[i + 1]:
            print("duplicate present")
            return
    print("There are no duplicate")


my_array = [2, 6, 1, 7, 9, 4]
check_duplicate_in_sorted_array(my_array)
