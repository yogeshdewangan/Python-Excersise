# You are given a list of integers that may contain consecutive numbers. Your task is to write a Python script that processes this list and merges consecutive numbers into a range format while keeping isolated numbers as they are.
# Requirements:
# Sort the list in ascending order.
# Merge consecutive numbers into a range (e.g., [1, 2, 3, 5, 6, 8, 9, 10, 13] should become ["1-3", "5-6", "8-10", "13"]).
# Single numbers should remain as individual elements (e.g., 4 stays as "4").
# The output should be a list of strings where ranges are represented as "start-end" and single numbers as "number".


def get_range(mylist):
    final_list = []
    start_index = 0
    while start_index <= len(mylist) - 1:
        start_value = mylist[start_index]
        end_value = mylist[start_index]
        for i in range(start_index, len(mylist)):
            if i == len(mylist)-1:
                end_value = mylist[i]
                break
            if mylist[i] + 1 != mylist[i + 1]:
                end_value = mylist[i]
                break

        if mylist.index(start_value) == mylist.index(end_value):
            final_list.append(str(start_value))
        else:
            final_list.append(str(start_value) + "-" + str(end_value))
        print(final_list)
        start_index = mylist.index(end_value) + 1
        pass

    return final_list


mylist = [1, 2, 3, 5, 6, 8, 9, 10, 13, 15,16]
print(get_range(mylist))


# ChatGPT Solution

def merge_consecutive_numbers(nums):
    if not nums:
        return []

    nums = sorted(set(nums))  # Sort and remove duplicates
    result = []
    start = nums[0]
    prev = nums[0]

    for num in nums[1:]:
        if num == prev + 1:
            prev = num
        else:
            if start == prev:
                result.append(f"{start}")
            else:
                result.append(f"{start}-{prev}")
            start = prev = num

    # Append the last processed range or number
    if start == prev:
        result.append(f"{start}")
    else:
        result.append(f"{start}-{prev}")

    return result


# Example usage
nums = [1, 2, 3, 5, 6, 8, 9, 10, 13]
print(merge_consecutive_numbers(nums))

