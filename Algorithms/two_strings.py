"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.

Example
s1= "and"
s2= "art"

These share the common substring "a"
s1= "be"
s2= "cat"

These do not share a substring.
ask (c) 2022. All rights reserved.
"""
from collections import Counter


def twoStrings(s1, s2):
    if not s1 or not s2:
        return "NO"

    frequency = Counter(s1)

    for i in s2:
        if i in frequency:
            return "YES"

    return "NO"


if __name__ == "__main__":
    print(twoStrings("Hello", "world"))
