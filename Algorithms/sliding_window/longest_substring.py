"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
ask (c) 2022. All rights reserved.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        longest = 1

        left = 0
        n = len(s)

        for i in range(1, n):
            if s[i] in s[left:i]:
                while s[left] != s[i]:
                    left += 1
                left += 1
            else:
                if longest < i - left + 1:
                    longest = i - left + 1

        return longest


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("au"))
print(Solution().lengthOfLongestSubstring("bwf"))
