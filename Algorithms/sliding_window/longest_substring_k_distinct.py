"""

ask (c) 2022. All rights reserved.
"""
map = {}


def add_element(element):
    if element in map:
        map[element] += 1
    else:
        map[element] = 1


def remove_element(element):
    if element in map:
        map[element] -= 1
        if map[element] == 0:
            map.pop(element)


def longest_substring(string, k):
    max_length = 0
    i = 0

    for j in range(len(string)):
        add_element(string[j])
        while len(map) > k:
            remove_element(string[i])
            i += 1
        current_length = j - i + 1
        max_length = max(current_length, max_length)
    return max_length


print(longest_substring("AAAHHHHHIBC", 2))
