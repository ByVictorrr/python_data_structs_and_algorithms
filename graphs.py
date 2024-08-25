class ListOfEdgesGraph:
    def __init__(self, num_of_nodes: int, directed=True):
        self._num_of_nodes = num_of_nodes
        self._directed = directed
        # List of Edges Graph representation
        self._list_of_edges = []

    def add_edge(self, node1, node2, weight=1):
        self._list_of_edges.append([node1, node2, weight])
        # undirected
        if not self._directed:
            self._list_of_edges.append([node2, node1, weight])

    def __str__(self):
        return "\n".join([str(e) for e in self._list_of_edges])


class AdjacencyMatrixGraph:

    def __init__(self, num_of_nodes: int, directed=True):
        self._num_of_nodes = num_of_nodes
        self._directed = directed
        # Init the adj matrix - nxn
        self._adj_matrix = [[0 for _ in range(num_of_nodes)] for _ in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self._adj_matrix[node1][node2] = weight
        # undirected
        if not self._directed:
            self._adj_matrix[node2][node1] = weight

    def __str__(self):
        return "\n".join([f"{n}: {self._adj_matrix[n]}" for n in range(self._num_of_nodes)])


class AdjacencyListGraph:

    def __init__(self, num_of_nodes: int, directed=True):
        self._num_of_nodes = num_of_nodes
        self._directed = directed
        # Init the adj list like a linked list
        self._adj_list = {node: set() for node in range(num_of_nodes)}

    def add_edge(self, node1, node2, weight=1):
        self._adj_list[node1].add((node2, weight))
        # undirected
        if not self._directed:
            self._adj_list[node2].add((node1, weight))

    def __str__(self):
        return str(self._adj_list)


if __name__ == "__main__":
    edges = [(0, 0, 25), (0, 1, 5), (0, 2, 3), (1, 3, 1), (1, 4, 15), (4, 2, 7), (4, 3, 11)]
    list_edges = ListOfEdgesGraph(5)
    for e in edges:
        list_edges.add_edge(*e)
    print(f"List of Edges:\n{list_edges}")
    adj_matrix = AdjacencyMatrixGraph(5)
    for e in edges:
        adj_matrix.add_edge(*e)
    print(f"Adjacency Matrix:\n{adj_matrix}")
    adj_list = AdjacencyListGraph(5)
    for e in edges:
        adj_list.add_edge(*e)
    print(f"Adjacency List:\n{adj_list}")
