from pip._vendor.distlib.compat import raw_input


def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)

if __name__=="__main__":
    n = int(raw_input())
    print(fac(n))
