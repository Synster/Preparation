"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none)
deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde"
while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for i in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):

                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]

    def lcs_recursive(self, text1: str, text2: str):

        n = len(text1)
        m = len(text2)

        if m == 0 or n == 0:
            return 0

        if text1[n - 1] == text2[m - 1]:
            return 1 + self.lcs_recursive(text1[: n - 1], text2[:m - 1])
        else:
            return max(self.lcs_recursive(text1[: n], text2[:m - 1]), self.lcs_recursive(text1[: n - 1], text2[:m]))

    def lcs_recursive_memo(self, text1: str, text2: str, dp):

        n = len(text1)
        m = len(text2)

        if m == 0 or n == 0:
            return 0

        if (text1, text2) in dp:
            return dp[(text1, text2)]

        if text1[n - 1] == text2[m - 1]:
            dp[(text1, text2)] = 1 + self.lcs_recursive(text1[: n - 1], text2[:m - 1])
        else:
            dp[(text1, text2)] = max(self.lcs_recursive(text1[: n], text2[:m - 1]),
                                     self.lcs_recursive(text1[: n - 1], text2[:m]))

        return dp[(text1, text2)]

    def lcs(self, text1: str, text2: str):
        # Tabulation
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]


print(Solution().longestCommonSubsequence("abcd", "bbcd"))
print(Solution().lcs_recursive("abcd", "bbcd"))
print(Solution().lcs_recursive_memo("abcd", "bbcd", {}))
print(Solution().lcs("abcd", "bbcd"))
