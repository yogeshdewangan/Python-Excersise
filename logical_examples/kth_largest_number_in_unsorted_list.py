import random
def solution(inputArray, k):
    pos = random.randint(0, len(inputArray) - 1)
    left = []
    right = []

    if len(inputArray) == 1:
        return inputArray[0]

    for i in range(len(inputArray)):
        if inputArray[i] <= inputArray[pos]:
            left.append(inputArray[i])
        else:
            right.append(inputArray[i])

    sorted_list = []

    if len(left) != 0:
        num = solution(left, k)
        sorted_list.append(num)
    if len(right) != 0:
        num = solution(right, k)
        sorted_list.append(num)

    return sorted_list


lst = [1, 4, 10, 5, 2]
k = 1
print(solution(lst,k))
