def merge(nums1, m, nums2, n):
    nums1 = [x for x in nums1 if x != 0]
    nums1.extend(nums2)
    nums1.sort()
    return nums1


nums1 = [1, 2, 3]
nums2 = [2, 4, 8]
m = 3
n = 3

nums3 = merge(nums1, m, nums2, n)

pass
