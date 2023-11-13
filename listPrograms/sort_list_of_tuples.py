"""
Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

"""

list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(list)):
    for j in range(len(list) - 1):
        if list[j][1] > list[j + 1][1]:
            list[j], list[j + 1] = list[j + 1], list[j]

print(list)

# Another way

list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def last(n):
    return n[-1]


def sort_list_tuple_by_last_key(list):
    return sorted(list, key=last)


print(sort_list_tuple_by_last_key(list))

# # Based on first value in tuples
# def first(n):
#     return n[0]
#
# def sort_list_tuple_by_last_key(list):
#     return sorted(list, key=first)
#
# print(sort_list_tuple_by_last_key(list))
#
#
