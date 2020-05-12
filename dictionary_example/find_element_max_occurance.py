my_array = [1,1,2,2,2,3,5,3,3,1,3,3,3,3,4,4,5,5,5,5,5,5,5,5,5,5]


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
