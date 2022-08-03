"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
Calculate the sum of that subset. It is possible that the maximum sum is 0, the case when all elements are negative.

Example

The following subsets with more than  element exist.
These exclude the empty subset and single element subsets which are also valid.

ask (c) 2022. All rights reserved.
"""


def max_sub_set_sum(arr):
    n = len(arr)
    dp = [[0, 0] for _ in range(n)]  # Define DP

    dp[0][0] = 0
    dp[0][1] = arr[0]  # Seed values

    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])  # Excl current ele = max of incl prev ele & excluding prev element
        dp[i][1] = dp[i - 1][0] + arr[i]  # Include current element = Exclude prev element + current element

    return max(dp[n - 1][0], dp[n - 1][1])


if __name__ == '__main__':
    print(max_sub_set_sum([-2, 1, 3, -4, 5]))
    print(max_sub_set_sum([3, 7, 4, 6, 5]))
    print(max_sub_set_sum([2, 1, 5, 8, 4]))
    print(max_sub_set_sum([3, 5, -7, 8, 10]))
