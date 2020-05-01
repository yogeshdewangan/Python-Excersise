def first_non_repeated_element(array):
    for i in range(len(array)):
        count=0
        for j in range(len(array)):
            if array[i]==array[j]:
                count+=1


        if count<=1:
            return array[i]


myarray= "aabbccdef"
print(first_non_repeated_element(myarray))