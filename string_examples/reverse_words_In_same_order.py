mystr = "I love my India"

list = mystr.split(' ')
new_str=""
for item in list:
    new_str +=item[::-1] +" "

print (new_str.strip())
