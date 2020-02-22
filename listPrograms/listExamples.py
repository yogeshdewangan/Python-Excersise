#Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.
def create_final_list_with_two_list():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [9, 8, 7, 6, 5, 4, 3, 2]

    print("First List - " + str(list1[1::2]))
    print("Second List - " + str(list2[0::2]))
    list3 = list()
    list3.extend(list1[1::2])
    list3.extend(list2[0::2])
    print("Final List - " + str(list3))

#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
def check_number_not_divisible_by():
    l = []
    for i in range(2000, 3201):
        if (i % 7 == 0) and (i % 5 != 0):
            l.append(str(i))

    print(','.join(str(i) for i in l))

if __name__ == "__main__":
    #create_final_list_with_two_list()
    #check_number_not_divisible_by()

    # list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(list1)
    # list1.pop(-1)
    # list1.pop(-2)
    # print(list1)

    x = ['ab', 'cd']
    print((list(map(list, x))))