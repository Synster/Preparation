"""

ask (c) 2022. All rights reserved.
"""
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": [],
}


def has_path_dfs(g, source, destination):
    stack = [source]

    while stack:
        current = stack.pop()
        if current == destination:
            return True
        neighbours = g[current]
        if neighbours:
            stack.extend(neighbours)
    return False


def has_path_dfs_recursive(g, source, destination):
    if source == destination:
        return True
    neighbours = g[source]
    for neighbour in neighbours:
        if has_path_dfs_recursive(g, neighbour, destination):
            return True
    return False


def has_path_bfs(g, source, destination):
    queue = [source]

    while queue:
        current = queue.pop(0)
        if current == destination:
            return True
        neighbours = g[current]
        if neighbours:
            queue.extend(neighbours)
    return False


print(has_path_bfs(graph, "a", "e"))
print(has_path_dfs(graph, "a", "e"))
print(has_path_dfs_recursive(graph, "a", "e"))
