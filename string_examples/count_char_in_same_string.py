"""
input = "aaabbacc"
output = "a3b2ac2"

"""

string = "aaabbcc"
coded = ''
while string:
    i = 0
    while i < len(string) and string[0] == string[i]:
        i += 1
    coded += string[0]+str(i)
    string = string[i:]

print(coded)