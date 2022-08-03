"""

ask (c) 2022. All rights reserved.
"""


def string_reversal(s):
    if not s:
        return ""

    return string_reversal(s[1:]) + s[0]


print(string_reversal("amandeep"))


def is_palindrome(s):
    if not s:
        return True

    if s[0] == s[-1]:
        return is_palindrome(s[1: -1])
    return False


print(is_palindrome("aman"))
print(is_palindrome("kayak"))
