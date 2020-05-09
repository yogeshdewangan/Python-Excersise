
mystr = "www.google.com"

dict = {}

for char in mystr:
    if char in dict.keys():
        dict[char]+=1
    else:
        dict[char]= 1

print dict