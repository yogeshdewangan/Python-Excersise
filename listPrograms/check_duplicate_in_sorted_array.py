def check_duplicate_in_sorted_array(my_array):
    my_array.sort()
    for i in range(len(my_array) - 1):
        if my_array[i] == my_array[i + 1]:
            print("duplicate present")
            return
    print("There are no duplicate")


def another_way(list):
    list1=[]
    count=1
    for item in list:
        if item in list1:
            count+=1
        else:
            list1.append(item)
        if count >1:
            print ("duplicate present")
            return

    print("There are no duplicate")


my_array = [2, 6, 1, 7, 9, 4]
check_duplicate_in_sorted_array(my_array)
another_way(my_array)
