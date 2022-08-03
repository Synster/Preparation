"""

ask (c) 2022. All rights reserved.
"""
edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]


def get_adjacency_list(edges):
    graph = {}
    for k, v in edges:
        add_edge(graph, k, v)
        add_edge(graph, v, k)  # Undirected graph
    return graph


def add_edge(graph, k, v):
    if k not in graph:
        graph[k] = []
    graph[k].append(v)


def has_path(graph, source, destination, visited):
    if source == destination:
        return True
    if source in visited:
        return False

    visited.add(source)

    neighbours = graph[source]

    for neighbour in neighbours:
        if has_path(graph, neighbour, destination, visited):
            return True
    return False


print(has_path(get_adjacency_list(edges), "i", "m", set()))

print(get_adjacency_list(edges))
