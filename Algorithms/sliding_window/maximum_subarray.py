"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""


def maximum_subarray(arr):
    current_max = arr[0]
    total_max = arr[0]

    for i in range(1, len(arr)):
        current_max = max(arr[i], current_max + arr[i])
        total_max = max(current_max, total_max)

    return total_max


print(maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 (4,-1,2,1)


def maximum_subarray_size3(arr):
    current_max = sum(arr[:3])
    total_max = sum(arr[:3])

    for i in range(3, len(arr)):
        current_max = current_max + arr[i] - arr[i - 3]
        total_max = max(current_max, total_max)

    return total_max


print(maximum_subarray_size3([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


def maximum_subarray_size_k(arr, k):
    current_max = sum(arr[:k])
    total_max = sum(arr[:k])

    for i in range(k, len(arr)):
        current_max = current_max + arr[i] - arr[i - k]
        total_max = max(current_max, total_max)

    return total_max


print(maximum_subarray_size_k([-2, 1, -3, 4, -1, 2, 1, -5, 4], 3))
print(maximum_subarray_size_k([-2, 1, -3, 4, -1, 2, 1, -5, 4], 4))
