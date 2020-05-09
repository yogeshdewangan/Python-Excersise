
"""
tuple is immutable, we can not add or delete items in tuple.
We can add 2 tuples in a new tuple.
Faster than list because of its static in nature
"""

tup = (3,4,2,7,5,6,9)
tup2= (34,454)

tup1 =tup.__add__(tup2)

print tup1