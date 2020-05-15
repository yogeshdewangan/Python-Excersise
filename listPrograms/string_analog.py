str1 = "petal"
str2 = "plate"


def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if (sorted_str1 == sorted_str2):
        print("Strings are anagram")
    else:
        print("String are not anagram")




dict1 = {'p': 1, 'e': 2, 't': 1, 'a': 1, 'l': 1}




for char in str2:
    if char in dict1.keys():
        dict1[char] = dict1[char] - 1
        if dict1[char] == 0:
            del dict1[char]

    else:
        print("not anagram")

if len( dict1) == 0:
    print ("anagram")
else:
    print("not anagram")










