s = "yogeshyogkumar"

import re

r = re.split(s, 'y')  # will print [y]
print(r)

r = re.split('yog', s)  # will print ['', 'esh', 'kumar']
print(r)

# sub

r = re.sub('yog', 'k', s)
print(r)


#subn

r = re.subn('yog', 'k', s)
print(r)


