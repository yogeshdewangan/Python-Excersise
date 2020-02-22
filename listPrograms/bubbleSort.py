def bubble_sort(list):
    for i in range(len(list)):
        for k in range(len(list) - i - 1):
            if list[k] > list[k + 1]:
                temp = list[k]
                list[k] = list[k + 1]
                list[k + 1] = temp
    return list


def bubble_sort1(list):
    for i in range(len(list)):
        for k in range(0, len(list) - 1):
            if list[k] > list[k + 1]:
                temp = list[k]
                list[k] = list[k + 1]
                list[k + 1] = temp
    return list

if __name__ == "__main__":
    list = [10, 20, 5, 3, 8, 38, 52, 4, 5]
    print(bubble_sort1(list))
