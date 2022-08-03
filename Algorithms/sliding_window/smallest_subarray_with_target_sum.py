"""

ask (c) 2022. All rights reserved.
"""


def smallest_subarray(nums, target):
    i, j = 0, 1
    current_sum = nums[0]
    best_length = len(nums)

    while j < len(nums):
        if current_sum + nums[j] < target:
            current_sum += nums[j]
            j += 1
        else:
            length = j - i + 1
            best_length = min(best_length, length)
            current_sum -= nums[i]
            i += 1

    return best_length


print(smallest_subarray([2, 3, 4, 5, 7, 8, 3], 8))
