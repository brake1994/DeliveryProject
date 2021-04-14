from HashTable import ChainingHashTable


# Class for a weighted graph. Used to store adjacency data between nodes and their weights.
class WeightedGraph:

    def __init__(self):
        self.vertices = []
        self.edges = ChainingHashTable(27)
        self.distances = ChainingHashTable(27)
        self.prev_vertices = ChainingHashTable(27)

    # Add vertex to vertices table
    # O(N) - searches through all vertices
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)

    # Add edges to edge table and edge/weight to distance table
    # O(1)
    def add_edge(self, start_vert, end_vert, distance):
        self.distances.insert((start_vert, end_vert), float(distance))
        self.distances.insert((end_vert, start_vert), float(distance))
        self.edges.insert(start_vert, end_vert)
        self.edges.insert(end_vert, start_vert)
