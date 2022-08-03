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
        return False

    visited.add((i, j))

    neighbors = get_neighbours(graph, row, col, i, j, visited)

    for x, y in neighbors:
        explore(graph, row, col, x, y, visited)
    return True


def island_count(graph, ) -> int:
    visited = set()
    count = 0

    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        for j in range(col):
            if explore(graph, row, col, i, j, visited):
                count += 1
    return count


grid = [
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'l', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'l', 'w'],
    ['w', 'w', 'l', 'l', 'w'],
    ['l', 'w', 'w', 'l', 'l'],
    ['l', 'l', 'w', 'w', 'w']
]

print(island_count(grid))
