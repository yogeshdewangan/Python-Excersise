def selectionsort(list):

    for i in range(len(list)):
        smallest=i
        for j in range(i+1, len(list)):
            if list[i]> list[j]:
                smallest=j

        list[i], list[smallest]= list[smallest], list[i]

    print(list)


if __name__ == "__main__":
    list = [3, 8, -1, 5, 9, -6, 4, 5]

    selectionsort(list)

worst_complexity = "O(n^2)"
