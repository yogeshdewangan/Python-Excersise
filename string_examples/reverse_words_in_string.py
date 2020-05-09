mystr= "I love my India"

list = mystr.split()
new_str =""

for word in list:
    new_str=" "+ word+new_str

print new_str
