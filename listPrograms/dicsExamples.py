from pip._vendor.distlib.compat import raw_input


def main():
    num =int(raw_input)
    d= dict()
    for i in range(1, num+1):
        d[i]=i*i


if __name__=="__main__":
    main()