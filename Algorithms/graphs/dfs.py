"""
Depth first search
-> Use stack

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


def dfs(g, source):
    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        neighbours = g[current]
        if neighbours:
            stack.extend(neighbours)





def dfs_recursive(g, source):
    print(source)
    neighbours = g[source]
    for neighbour in neighbours:
        dfs_recursive(g, neighbour)


def bfs(g, source):
    queue = [source]

    while queue:
        current = queue.pop(0)
        print(current)
        neighbours = g[current]
        if neighbours:
            queue.extend(neighbours)


print("DFS")
dfs(graph, "a")
print("DFS Recursive")
dfs(graph, "a")
print("BFS")
bfs(graph, "a")
print("Topological Sort")
