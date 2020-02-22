from pip._vendor.distlib.compat import raw_input


def main():
    num = int(raw_input("Number"))
    check_num_pelindrom(num)

def check_num_pelindrom(num):
    num1 = num
    new_num = 0
    while (num > 0):
        dig = num % 10
        new_num=dig + new_num * 10
        num= num//10

    if num1 == new_num:
        print("Number is pelindrome")


if __name__ == "__main__":
    main()
