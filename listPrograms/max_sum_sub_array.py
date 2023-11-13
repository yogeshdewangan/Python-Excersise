def max_sub_arry(arr_int):
    count = 0
    temp_count = 0

    start =0
    end = 0

    temp_start = 0
    temp_end = 0

    for i in range(len(arr_int)):
        temp_count = temp_count + arr_int[i]
        temp_end = i
        if temp_count < 0:
            temp_count =0
            temp_start = temp_start + 1
        if count < temp_count:
            count = temp_count
            start = temp_start
            end = temp_end

    print(count, arr_int[start:end+1])

arr_int1 = [-3,5,2,1,-3,4,-1,2,1,-5,4,0,2,1,-9,-11]
arr_int2 = [-3,5,2,1,-3,4,-30,-1,2,1,-5,4,0,2,1,-9,-11]
arr_int3 = [-3,5,2,1,-3,4,-1,2,1,-5,4,14,-14,20,0,2,1,-9,11, -30, 50]

max_sub_arry(arr_int1)
max_sub_arry(arr_int2)
max_sub_arry(arr_int3)