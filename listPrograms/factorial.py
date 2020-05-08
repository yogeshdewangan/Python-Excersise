from pip._vendor.distlib.compat import raw_input


def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)



def fact_without_recurssion(n):
    result = 1
    for i in range(n, 0, -1):
        result *= i
    return result


if __name__=="__main__":
    n = int(raw_input())
    # print(fac(n))
    print(fact_without_recurssion(n))
