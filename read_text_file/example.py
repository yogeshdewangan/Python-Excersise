

with open("txt.txt") as txt_file:
    for line in txt_file:
        print(line)


"""
if there is a large amount of data in a single line then it will use a lot of memory. 
In that case, we can read the file content into a buffer and process it.
"""

with open("txt.txt") as text_file:
    while True:
        line_break = text_file.read(1024)
        if not line_break:
            break;
        print(line_break)


"""
Check file size
"""
import os
print("File size:" + str(os.stat("txt.txt").st_size))

