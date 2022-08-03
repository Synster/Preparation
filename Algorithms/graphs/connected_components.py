"""

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
        return False

    visited.add(source)

    neighbours = graph[source]

    for neighbour in neighbours:
        dfs(graph, neighbour, visited)
    return True


def connected_components(graph: dict) -> int:
    visited = set()
    count = 0
    for key in graph.keys():
        if dfs(graph, key, visited):
            count += 1

    return count


print(connected_components(graph))