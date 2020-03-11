from unicodedata import decimal

string = "In 2020, the avg temperatures in bangalore were variying from 15-25.30. The humidity also increased from 50.5% to 70.24%."


import re
list = re.findall("[0-9]+\.?[0-9]+", string)
print(list)
sum =0
for i in list:
    sum =sum+float(i)

print(sum)
