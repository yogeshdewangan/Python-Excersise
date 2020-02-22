
string="Hello from shu.bhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM"

import re
print(re.findall("\S+@\S+",string))

string="my 1 home and 2 kids have 100 toys"
print(re.findall('[0-9]+', string))