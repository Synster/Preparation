"""

(i) ---- (j)
|
|
|
(k) ---- (l)
|
|
|
(m)

(o) --- (n)

ask (c) 2022. All rights reserved.
"""
graph = {
    'i': ['j', 'k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}


def dfs(graph, source, visited):
    if source in visited:
        return 0

    visited.add(source)
    count = 1
    neighbours = graph[source]

    for neighbour in neighbours:
        count += dfs(graph, neighbour, visited)
    return count


def largest_connected_components(graph: dict) -> int:
    visited = set()
    max_count = 0
    for key in graph.keys():
        count = dfs(graph, key, visited)
        if count > max_count:
            max_count = count

    return max_count


print("Largest Connected Component Size: {}".format(largest_connected_components(graph)))
