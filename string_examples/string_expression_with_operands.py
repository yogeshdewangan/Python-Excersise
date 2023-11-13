mystr = "2*6/3+4-3+4/2"  # 2*2+4-3+2  # 4+4-5 =1
mystr = list(mystr)
def remove_empty(mylist):
    while ("" in mylist):
        mylist.remove("")

def cal_ind(mystr, opr):
    for i in range(len(mystr)):
        if mystr[i] == opr:
            if opr == '/':
                mystr[i] = str(int(mystr[i - 1]) // int(mystr[i + 1]))
            if opr == '*':
                mystr[i] = str(int(mystr[i - 1]) * int(mystr[i + 1]))
            if opr == '+':
                mystr[i] = str(int(mystr[i - 1]) + int(mystr[i + 1]))
            if opr == '-':
                mystr[i] = str(int(mystr[i - 1]) - int(mystr[i + 1]))
            mystr[i - 1] = ''
            mystr[i + 1] = ''
    remove_empty(mystr)

cal_ind(mystr, '/')
cal_ind(mystr, '*')
cal_ind(mystr, '+')
cal_ind(mystr, '-')

print(mystr[0])


