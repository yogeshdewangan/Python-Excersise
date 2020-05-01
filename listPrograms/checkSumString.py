def main():
    str1 = "12243660"
    is_sum_string=False
    for i in range(1, 5):
        list = []
        for j in range(0, len(str1), i):
            list.append(str1[j:j + i])
        all_fine = False
        for k in range(0, len(list)):
            if k + 2 < len(list):
                if int(list[k]) + int(list[k + 1]) == int(list[k + 2]):
                    all_fine = True
                else:
                    all_fine = False
                    break

        if all_fine == True:
            is_sum_string=True
            break
        else:
            is_sum_string=False
    if is_sum_string == True:
        print("Sum string")

    else:
        print("Not a Sum string")


if __name__ == "__main__":
    main()
