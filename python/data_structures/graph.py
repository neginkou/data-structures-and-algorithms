class Vertex:
    def __init__(self, value):
        self.value = value

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        node = Vertex(value)
        if node.value not in self._adjacency_list:
            self._adjacency_list[node.value] = []
        return node

    def add_edge(self, start, end):
        if start.value in self._adjacency_list and end.value in self._adjacency_list:
            self._adjacency_list[start.value].append(end.value)
            self._adjacency_list[end.value].append(start.value)  # Assuming an undirected graph

    def get_nodes(self):
        return [Vertex(vertex) for vertex in self._adjacency_list.keys()]

    def breadth_first(self, start):
        queue = [start]
        visited = set()
        result = []

        while queue:
            current = queue.pop(0)
            if current.value not in visited:
                visited.add(current.value)
                result.append(current.value)
                queue.extend([Vertex(neighbor) for neighbor in self._adjacency_list[current.value]])

        return result
