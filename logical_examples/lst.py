import random


def solution(inputArray, k):
    pos = random.randint(0, len(inputArray) - 1)
    left = []
    right = []

    nonlocal array

    if len(inputArray) == 1:
        return inputArray[0]

    for i in range(len(inputArray)):
        if inputArray[i] <= inputArray[pos]:
            left.append(inputArray[i])
        else:
            right.append(inputArray[i])

    if len(right) != 0:
        num = solution(right, k, array)
        if num != None and num not in array:
            array.append(num)

    if len(left) != 0:
        num = solution(left, k, array)
        if num != None and num not in array:
            array.append(num)

    try:
        return array[k - 1]

    except:
        pass


print(solution([19, 32, 11, 23], 3))