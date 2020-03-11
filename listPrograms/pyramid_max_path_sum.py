"""
 you have a pyramid built of numbers from an array. Eg: [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]), like this one here:
       3
      7 4
     2 4 6
    8 5 9 3

    Task is  to find the  maximum sum of consecutive numbers from the top to the bottom of the pyramid by making a downward step either to the right or left.  The longest slide down value is 3 + 7 + 4 + 9 = 23
       /3/
      \7\ 4
     2 \4\ 6
    8 5 \9\ 3

"""


def get_sum_max_path(list, previous_found_index):
    if len(list) > previous_found_index + 1:
        if list[previous_found_index] < list[previous_found_index + 1]:
            sum = list[previous_found_index + 1]
            index = previous_found_index + 1
        else:
            sum = list[previous_found_index]
            index = previous_found_index
    else:
        sum = list[previous_found_index]
        index = previous_found_index
    return sum, index


list_of_list = [[3], [7, 4], [2, 4, 6], [8, 9, 5, 3]]
sum_num = 0
index=0
for list in list_of_list:
    sum, index = get_sum_max_path(list, index)
    sum_num += sum
print(sum_num)































