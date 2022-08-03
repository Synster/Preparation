"""
Graph representation using Adjacency List

Pros:
    Saves space O(|V|+|E|) . Worst case, there can be C(V, 2) number of edges in a graph thus consuming O(V^2) space.
    Adding a vertex is easier.
    Computing all neighbors of a vertex takes optimal time.
Cons:
    Queries like whether there is an edge from vertex u to vertex v are not efficient and can be done O(V).
    In Real-life problems, graphs are sparse(|E| <<|V|2). Adjacency lists Data structure is commonly used for storing graphs.
    Adjacency matrix will enforce (|V|2) bound on time complexity for such algorithms.

ask (c) 2022. All rights reserved.
"""


class Node:
    def __init__(self, val=None):
        self.value = val
        self.next = None

    def print(self):
        print(self.value)

    def __str__(self) -> str:
        return str(self.value)


class Graph:
    def __init__(self, vertex_count):
        self.adjacency_list = [None] * vertex_count
        self.vertex_count = vertex_count

    def add_edge(self, src, dest):
        node = Node(src)
        node.next = self.adjacency_list[dest]
        self.adjacency_list[dest] = node

        node = Node(dest)
        node.next = self.adjacency_list[src]
        self.adjacency_list[src] = node

    def print_graph(self):
        for index, vertex in enumerate(self.adjacency_list):
            temp = vertex
            print("Vertex {} head".format(index), end="")
            while temp:
                print(" -> {}".format(temp.value), end="")
                temp = temp.next
            print(" \n")


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
