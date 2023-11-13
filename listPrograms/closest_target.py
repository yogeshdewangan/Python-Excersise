def closest(lst, num):
    closest = lst[0]
    for i in range(1, len(lst)):
        if abs(lst[i] - num) < closest:
            closest = lst[i]
    print (closest)

    # wrong solution, not working


closest([3,8,9,4,1,12,2], 5)