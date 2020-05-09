my_array = [1,1,2,2,2,3,5,3,3,1,3,3,3,3,4,4,5,5,5,5,5,5,5,5,5,5]

def find_element_max_occurance(my_array):
    count=1
    max=1
    element= my_array[0]
    for i in range(1, len(my_array)):
        if my_array[i]==element:
            count+=1
            if count>max:
                max=count
                max_occrurance_element= element
        else:
            element= my_array[i]
            count=1
    print(max_occrurance_element, max)

find_element_max_occurance(my_array)


#using dictionary

def find_element_occurances_using_dict(array):
    dict={}
    for char in array:
        if char in dict.keys():
            dict[char]=dict[char]+1
        else:
            dict[char]=1

    print(dict)
    max_key = max(dict, key=dict.get)
    print(max_key)
    print(dict[max_key])

find_element_occurances_using_dict(my_array)
