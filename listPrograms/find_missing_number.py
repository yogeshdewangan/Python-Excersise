

from math import fsum


array=[2,1,3,6,4,7,8]


def find_missing_number(array):
    n= len(array)
    total = (n+1)*(n+2)/2
    sum = int(fsum(array))
    return int(total-sum)


print (find_missing_number(array))