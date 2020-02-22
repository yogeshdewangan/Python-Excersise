def first_non_repeated_element(array):
    duplicate_flag=False
    for i in range(0, len(array)):
        count=1
        for j in range(0, len(array)):
            if array[i]==array[j]:
                count+=1


        if count<=2:
            return array[i]


myarray= "aabbccdef"
print(first_non_repeated_element(myarray))