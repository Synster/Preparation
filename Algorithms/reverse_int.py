"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
ask (c) 2022. All rights reserved.
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 2 ** -31:
            return 0

        result = 0
        is_negative = x < 0
        x = abs(x)
        while x > 0:
            remainder = x % 10

            result = result * 10 + remainder
            x = x // 10

        return result * -1 if is_negative else result


print(Solution().reverse(-321))
print(Solution().reverse(321))
