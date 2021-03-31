# from code_challenges.graphs.graphs import Graph
# from code_challenges.stacks_and_queues.stacks_and_queues import Queue
class Node():
  def __init__(self, value, next = None):
    self.value = value
    self.next = next 

class InvalidOperationError(BaseException):
  pass

class Queue():
  def __init__(self, front = None):
    self.front = front
    self.rear = None

  def enqueue(self, value):
    node = Node(value)
    
    if self.is_empty():
      self.front = node
      self.rear = node
    else:
      self.rear.next = node  
      self.rear = node
    
  def dequeue(self):
    if self.is_empty():
      raise InvalidOperationError("Method not allowed on empty collection")
    temp = self.front
    self.front = self.front.next
    temp.next = None
    return temp.value
    
  def peek(self):
    if self.is_empty():
      raise InvalidOperationError("Method not allowed on empty collection")
    return self.front.value

  def is_empty(self):
    return self.front == None

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
    
    def breadth_first(self, vertex):
        nodes = []
        breadth = Queue()
        visited = set() 
        
        breadth.enqueue(vertex)
        visited.add(vertex)

        while breadth:
            front = breadth.dequeue()
            print(front)
            nodes.append(front)
            # print(self.get_neighbors(front))
            for neighbor in self.get_neighbors(front):
                # print(neighbor)
                if neighbor.vertex not in visited:
                    visited.add(neighbor)
                    breadth.enqueue(neighbor)
        
        return nodes


    # def __str__(self):
    #     return str(self._adjacency_list)
    
class Vertex:
    def __init__(self, value):
        self.value = value
    
    # def __str__(self):
    #     return str(self.value)

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

    # def __str__(self):
    #    return f"({self.vertex}, {self.weight})"

graph = Graph()
a = graph.add_node('a')
b = graph.add_node('b')
c = graph.add_node('c')
graph.add_edge(a, b)
graph.add_edge(a, c)
graph.breadth_first(a)

# class Graph(Graph):
#     def breadth_first(self, vertex):
#         nodes = []
#         breadth = Queue()
#         visited = set() 
        
#         breadth.enqueue(vertex)
#         visited.add(vertex)

#         while breadth:
#             front = breadth.dequeue()
#             nodes.append(front)

#             for neighbor in self.get_neighbors(front):
#                 print(neighbor)
#                 if neighbor.vertex not in visited:
#                     visited.add(neighbor)
#                     breadth.enqueue(neighbor)
        
#         return nodes
