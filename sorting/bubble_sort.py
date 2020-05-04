def bubblesort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) -1 ):
            if list[j] > list[j+1]:
                #another way of swapping
                list[j], list[j+1]= list[j+1], list[j]
    print(list)


if __name__ == "__main__":
    list = [3, 8, -1, 5, 9, -6, 4, 5]

    bubblesort(list)


worst_complexity= "O(n^2)"