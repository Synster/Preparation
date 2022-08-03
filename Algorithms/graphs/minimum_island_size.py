"""

ask (c) 2022. All rights reserved.
"""
"""
000000000
110000100
110001100
000000000
110000000

ask (c) 2022. All rights reserved.
"""


def get_neighbours(graph, row, col, i, j, visited):
    coordinates = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    neighbours = []
    for i, j in coordinates:
        if (0 <= i < row and 0 <= j < col) and (i, j) not in visited and graph[i][j] != 'w':
            neighbours.append((i, j))

    return neighbours


def explore(graph, row, col, i, j, visited) -> int:
    if graph[i][j] == 'w' or (i, j) in visited:
        return 0

    visited.add((i, j))
    size = 1
    neighbors = get_neighbours(graph, row, col, i, j, visited)

    for x, y in neighbors:
        size = size + explore(graph, row, col, x, y, visited)
    return size


def minimum_island_size(graph, ) -> int:
    visited = set()

    row = len(grid)
    col = len(grid[0])
    min_island_size = row * col
    for i in range(row):
        for j in range(col):
            island_size = explore(graph, row, col, i, j, visited)
            if island_size != 0 and island_size < min_island_size:
                min_island_size = island_size
    return min_island_size


grid = [
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'w'],
    ['w', 'w', 'l', 'l', 'w'],
    ['l', 'w', 'w', 'l', 'l'],
    ['l', 'l', 'w', 'w', 'w']
]

print(minimum_island_size(grid))
