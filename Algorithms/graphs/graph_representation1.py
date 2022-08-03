"""
A simple representation of graph using Adjacency Matrix

Pros:
    Removing an edge takes O(1) time.
    Queries like whether there is an edge from vertex ‘u’ to vertex ‘v’ are efficient and can be done O(1).

Cons:
    Consumes more space O(V^2).
    Even if the graph is sparse, it consumes the same space.
    Adding a vertex is O(V^2) time.
    Computing all neighbors of a vertex takes O(V) time (Not efficient).

ask (c) 2022. All rights reserved.
"""


class Graph:
    def __init__(self, vertex_count):
        self.matrix = [[-1] * vertex_count for _ in range(vertex_count)]  # Adjacency Matrix
        self.vertices = [-1] * vertex_count  # Keeps a list of vertex name
        self.vertex_index_map = {}  # map of vertex name to index
        self.vertex_count = vertex_count

    def set_vertex(self, index, name):
        if 0 <= index <= self.vertex_count:
            self.vertex_index_map[name] = index  # add the vertex name to index mapping a->0
            self.vertices[index] = name  # add the vertex name to list

    def set_edge(self, frm, to, cost=0):
        frm = self.vertex_index_map[frm]  # find the index of from vertex
        to = self.vertex_index_map[to]  # find the index of to vertex
        self.matrix[frm][to] = cost  # Mark the edge in the matrix
        self.matrix[to][frm] = cost  # Mark the reverse edge in the matrix, skip in DAG

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        edges = []
        for i in range(self.vertex_count):
            for j in range(self.vertex_count):
                if self.matrix[i][j] != -1:
                    edges.append((self.vertices[i], self.vertices[j], self.matrix[i][j]))
        return edges

    def get_graph(self):
        return self.matrix

    def print_graph(self):
        for row in self.matrix:
            print(row)


G = Graph(6)
G.set_vertex(0, 'a')
G.set_vertex(1, 'b')
G.set_vertex(2, 'c')
G.set_vertex(3, 'd')
G.set_vertex(4, 'e')
G.set_vertex(5, 'f')
G.set_edge('a', 'e', 10)
G.set_edge('a', 'c', 20)
G.set_edge('c', 'b', 30)
G.set_edge('b', 'e', 40)
G.set_edge('e', 'd', 50)
G.set_edge('f', 'e', 60)
print("Vertices of Graph")
print(G.get_vertices())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
G.print_graph()
