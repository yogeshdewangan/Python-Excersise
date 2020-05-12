def bubble_sort(list):
    for i in range(len(list)):
        for k in range( len(list) -1 ):
            if list[k] > list[k + 1]:
                list[k], list[k + 1] = list[k + 1], list[k]

    return list


if __name__ == "__main__":
    list = [10, 20, 5, 3, 8, 38, 52, 4, 5]
    print(bubble_sort(list))
