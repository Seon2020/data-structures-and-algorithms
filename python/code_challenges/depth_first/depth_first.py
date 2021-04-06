from code_challenges.graphs.graphs import Graph
from code_challenges.stacks_and_queues.stacks_and_queues import Stack

class Graph(Graph):
    def depth_first(self, vertex):
        result = [vertex]
        stack = Stack()
        stack.push(vertex)
        while not stack.is_empty():
            peek = stack.peek()
            neighbors = self.get_neighbors(peek)
            not_visited = []
            for node in neighbors:
                if node.vertex not in result:
                    not_visited.append(node.vertex)
            if len(not_visited) > 0:
                result.append(not_visited[0])
                stack.push(not_visited[0])
            else: stack.pop()

        return result