def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":

    n =10
    for i in range(5):
        print(fibo(i))
