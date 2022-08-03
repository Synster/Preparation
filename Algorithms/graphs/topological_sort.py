"""

ask (c) 2022. All rights reserved.
"""


def topological_sort_util(g, source, visited, stack):
    visited.add(source)

    neighbours = g[source]
    for v in neighbours:
        if v not in visited:
            topological_sort_util(g, v, visited, stack)

    stack.append(source)


def topological_sort(g):
    visited = set()
    stack = []
    for v in g.keys():
        if v not in visited:
            topological_sort_util(g, v, visited, stack)

    return stack[::-1]


graph2 = {0: [],
          1: [],
          2: [3],
          3: [1],
          4: [0, 1],
          5: [0, 2]}

print("Topological Sort")
print(topological_sort(graph2))
