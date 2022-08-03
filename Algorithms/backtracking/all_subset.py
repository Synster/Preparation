"""

ask (c) 2022. All rights reserved.
"""
from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        state = []
        self.search(state, solutions, nums)
        return solutions

    def get_candidates(self, state, nums):
        # Only the array remaining after the last used element are valid options
        if not state:
            return nums.copy()

        last_element = state[-1]
        candidate = nums[nums.index(last_element)+1:]
        return candidate

    def search(self, state, solutions, nums):
        # IsValidState is not needed because we are creating only valid subsets
        solutions.append(state.copy())
        # return Can't return here because we need all subsets

        for candidate in self.get_candidates(state, nums):
            state.append(candidate)
            self.search(state, solutions, nums)
            state.remove(candidate)


print(Solution().subsets([1, 2, 3]))
print(Solution().subsets([0]))
print(Solution().subsets([3, 9]))
print(Solution().subsets([4, 1, 0]))
print(Solution().subsets([1, 2, 3, 4, 5, 6, 7, 8, 10, 0]))
