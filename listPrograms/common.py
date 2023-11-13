def solution(s1, s2):
    s1_dict = count_char(s1)
    s2_dict = count_char(s2)
    count = 0
    for k in s1_dict.keys():
        if k in s2_dict.keys():
            if s1_dict[k] == s2_dict[k]:
                count += s1_dict[k]
    return count


def count_char(s1):
    mydict = {}
    for char in s1:
        if char in mydict.keys():
            mydict[char] += 1
        else:
            mydict[char] = 1
    return mydict


print(solution("aabcc", "adcaa"))