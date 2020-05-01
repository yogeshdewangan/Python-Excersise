def insertionsort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key
    print(list)


if __name__ == "__main__":
    list = [3, 8, -1, 5, 9, -6, 4, 5]

    insertionsort(list)

worst_complexity = "O(n^2)"
