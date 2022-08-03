"""

ask (c) 2022. All rights reserved.
"""


class Graph:
    def __init__(self, vertices):
        self.graph = {}
        for i in range(vertices):
            self.add_node(i)

    def add_node(self, node):
        self.graph[node] = []

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def print_graph(self):
        for key, value in self.graph.items():
            print("Vertex {} head -> {}".format(key, value))


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
