"""
Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
"""

list = ['abc','aba','xcv','1921','a']

count =0

for item in list:
    if len(item)>0 and item[0] == item[len(item)-1]:
        count+=1

print(count)
