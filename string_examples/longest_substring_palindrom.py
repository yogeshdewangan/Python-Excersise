# Given a string, find the longest substring which is a palindrome
# input s = “aabbccdeedccbaa”  output - bccdeedccb


str = "aabbccdeedccbaa"
str = "aabbccdeedc1cbaabc1cdeedc"
longest = ""
length = len(str)
my_dict = {}

for i in range(length):
    for j in range(i+1, length+1):
        temp = str[i:j]
        if temp == temp[::-1]:
            if len(temp) > len(longest):
                longest = temp

print(longest)