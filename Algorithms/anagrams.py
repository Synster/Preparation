"""
Check if given 2 strings are anagrams

ask (c) 2022. All rights reserved.
"""
from collections import Counter


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    if not s1 or not s2:
        return False

    return sorted(s1) == sorted(s2)


def are_anagrams2(s1, s2):
    if len(s1) != len(s2):
        return False

    if not s1 or not s2:
        return False

    return Counter(s1) == Counter(s2)


print(are_anagrams("aman", "maan"))
print(are_anagrams2("aman", "maan"))
