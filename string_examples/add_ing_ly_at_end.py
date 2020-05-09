
mystr = "yo"
new_str =""
if len(mystr)<3:
    new_str = mystr
else:
    if mystr[-3:]=="ing":
        new_str= mystr+"ly"
    else:
        new_str=mystr+"ing"

print new_str