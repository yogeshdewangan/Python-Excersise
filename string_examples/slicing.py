import sys
"""
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[start:stop:step]  # start, stop and step
"""

mystr = "yogesh kumar dewangan"

print "last char: " + mystr[-1]

print "last three char: " + mystr[-3:]

print "last three char but not last one: " + mystr[-4:-1]

print "start stop and step: "+ mystr[3: 9: 1]

print "start stop and step: "+ mystr[3: 12: 2]

print "start stop and step: "+ mystr[-9:-2:2 ]

print "reverse the string: " + mystr[::-1]

