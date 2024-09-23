from queue import PriorityQueue, Queue


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
        self._adj_matrix = [[-1 for _ in range(num_of_nodes)] for _ in range(num_of_nodes)]
        self.visited = []

    def add_edge(self, node1, node2, weight=1):
        self._adj_matrix[node1][node2] = weight
        # undirected
        if not self._directed:
            self._adj_matrix[node2][node1] = weight

    def dijkstra(self, start_vertex):
        d = {v: float("inf") for v in range(self._num_of_nodes)}
        d[start_vertex] = 0
        pq = PriorityQueue()
        pq.put((0, start_vertex))
        while not pq.empty():
            _, current_vertex = pq.get()
            self.visited.append(current_vertex)
            for nbr in range(self._num_of_nodes):
                if self._adj_matrix[current_vertex][nbr] != -1:
                    distance = self._adj_matrix[current_vertex][nbr]
                    if nbr not in self.visited:
                        old_cost = d[nbr]
                        new_cost = d[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, nbr))
                            d[nbr] = new_cost
        return d

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

    def depth_first_search(self, start, target, path=[], visited=set()):
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        for nbr, _ in self._adj_list[start]:
            if nbr not in visited:
                if found_path := self.depth_first_search(nbr, target, path, visited):
                    return found_path

        path.pop()
        return None

    def non_weighted_bfs(self, start_node, target_node):
        # set of the vised nodes to prevent loops
        visited = set()
        _queue = Queue()
        # Addd the start_node to the queue and visited list
        _queue.put(start_node)
        visited.add(start_node)
        # start_node has not parents
        parent = dict()
        parent[start_node] = None
        path_found = False
        while not _queue.empty():
            current_node = _queue.get()
            if current_node == target_node:
                path_found = True
                break

            for nbr, _ in self._adj_list[current_node]:
                if current_node not in visited:
                    _queue.put(nbr)
                    parent[nbr] = current_node
                    visited.add(nbr)
        _paths = []
        if path_found:
            _paths.append(target_node)
            while not parent[target_node]:
                target_node = parent[target_node]
                _paths.append(target_node)
        return _paths

    def non_weighted_bf(self, start_node):
        visited = set()
        _queue = Queue()
        _queue.put(start_node)
        visited.add(start_node)
        while not _queue.empty():
            current_node = _queue.get()
            print(current_node, end=", ")
            for nbr, _ in self._adj_list[current_node]:
                if nbr not in visited:
                    _queue.put(nbr)
                    visited.add(nbr)

    def a_star_algorithm(self, start_node, stop_node, heuristic: dict):
        open_list, closed_list = {start_node}, set()
        # g contains current distances from `start_node` to all other nodes
        g = {start_node: 0}
        # parents contains an adjacency map of all nodes
        parents = {start_node: start_node}
        while len(open_list) > 0:
            n = None
            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if not n or g[v] + heuristic[v] < g[n] < heuristic[n]:
                    n = v
            if not n:
                print("Path does not exist!")
                return None
            # if the current node is the stop_node we being reconstruct the path from it to the start_node
            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print(f"Path found: {reconst_path}")
                return reconst_path
            # for all nbrs of the current node do
            for m, weight in self._adj_list[n]:
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                # check if its quicker to first vist n
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            # Remove n from the open_list, and add it to the closed_list b/ all neighbor were injected
            open_list.remove(n)
            closed_list.add(n)
        print(f"Path does not exist!")
        return None

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
    path = adj_list.depth_first_search(0, 4)
    print(f"0->4 path: {path}")
