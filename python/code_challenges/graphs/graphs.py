class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, val):
        v = Vertex(val)
        self._adjacency_list[v] = []
        return v
    
    def add_edge(self, start, end, weight=1):
        if start not in self._adjacency_list:
            raise KeyError('Start vertex not in graph!')
        if end not in self._adjacency_list:
            raise KeyError('End vertex not in graph!')
        edge = Edge(end, weight)
        adjacencies = self._adjacency_list[start]
        adjacencies.append(edge)
        return edge

    def get_nodes(self):
        return list(self._adjacency_list) or None

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def size(self):
        return len(self._adjacency_list)

    def __str__(self):
        return str(self._adjacency_list)
    
class Vertex:
    def __init__(self, value):
        self.value = value
    
class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

graph = Graph()
a = graph.add_node('a')
b = graph.add_node('b')
c = graph.add_node('c')
e_1 = graph.add_edge(a, b, 2)
print(e_1)
