"""

(v)---(w)
|      |
|      |
(z)   (x)
|      /
|    /
(y)
ask (c) 2022. All rights reserved.
"""
graph = {
    'v': ['w', 'z'],
    'w': ['v', 'x'],
    'x': ['w', 'y'],
    'y': ['x', 'z'],
    'z': ['v', 'y'],
}


def shortest_path(graph, source, destination):
    queue = [(source, 0)]
    visited = set()

    while queue:
        current, distance = queue.pop(0)

        if current == destination:
            return distance
        visited.add(current)
        neighbours = graph[current]
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            queue.append((neighbour, distance + 1))

    return -1


print("Shortest path: {}".format(shortest_path(graph, 'w', 'z')))
