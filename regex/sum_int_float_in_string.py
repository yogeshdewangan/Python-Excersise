from unicodedata import decimal

string = "In 2020, the avg temperatures in bangalore were variying from 15-25.30. The humidity also increased from 50.5% to 70.24%."


import re
list = re.findall("[0-9]+\.?[0-9]+", string)
list1 = re.findall("\d+\.?\d*", string)
#\S(\d+|^).?\d*
print(list)
sum =0
for i in list:
    sum =sum+float(i)

print(sum)

"""
.  --> matches any characters other than new line

\d --> matches any digit

\D --> matches any non-digit

\w --> matches any word characters (a-z, A-Z, 0-9, _)

\W --> matches any non-word characters (+, -, ?, ")

\s --> matches any white space characters (tab as well)

\S --> matches any non-white space characters


Anchors:
========

\b --> word boundary

word is "kumar"   then search can be "\bku" or "ar\b"
it cannot search middle of the word e.g. "\bum" wont search anything as "um" is middle word in "kumar"

\B --> not a word boundary

it can search middle of word, "\Bum" where "um" is middle of the word "kumar"

^  --> beginning of string

if "02341" then "^0"

$  --> end of string

if "02341" then "1$"


Quantifiers:
============

?  --> 1 or 0    eg. -? (1 hypen or zero hypen)

+  --> 1 or more   

*  --> 0 or more

{3} --> exact match of 3 repetitions

e.g.
=====
"\d{3}(-| )\d{3}(-| )\d{4}" will match "890-466-6082" and "890 466 6082"
"(-| )" match "-" or a space


OR operator
===========

|  -> Either this or that


Brackets:
=========

[]  --> matches characters in brackets
[^ ]  --> matches characters not in brackets



"""
