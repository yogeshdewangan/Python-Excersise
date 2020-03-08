
l1= ['2','10','5','4']
l1.sort()
print(l1)    #this will print ['10', '2', '4', '5'], it will sort the list based on ASCCI values


l1= [int(i) for i in l1]     # this will convert all elements to int first
l1.sort()       # and then this will sort the list
print(l1)       #