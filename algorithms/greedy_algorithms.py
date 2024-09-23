from dataclasses import dataclass
from queue import PriorityQueue


@dataclass
class Item:
    value: float
    weight: float

    # A utility function to calculate value to weight ratio
    def value_per_weight(self) -> float:
        return self.value / self.weight


def fractional_knapsack(capacity, items):
    """
    Function to solve the fractional knapsack problem.

    :param capacity: The maximum capacity of the knapsack.
    :param items: A list of Item objects, each with a value and weight.
    :return: The maximum value that can be obtained by filling the knapsack.
    """
    # Step 1: Sort items by value-to-weight ratio in decreasing order
    items.sort(key=lambda item: item.value_per_weight(), reverse=True)

    total_value = 0  # Total value accumulated in the knapsack
    current_weight = 0  # Current weight in the knapsack

    # Step 2: Loop through each item and add as much of it as possible to the knapsack
    for item in items:
        if current_weight + item.weight <= capacity:
            # If we can take the whole item, take it
            current_weight += item.weight
            total_value += item.value
        else:
            # If we can't take the whole item, take a fraction of it
            remaining_capacity = capacity - current_weight
            total_value += item.value_per_weight() * remaining_capacity
            current_weight += remaining_capacity
            break  # Knapsack is full

    return total_value


def return_machine_change(change, denominations):
    # make a list size of length denominations filled with 0
    to_give_back = [0] * len(denominations)
    # goes backward through denominations list
    # and also keeps track of the counter, pos
    for pos, coin in enumerate(reversed(denominations)):
        # while we can still use coin, use it until we can't
        while coin <= change:
            change -= coin
            to_give_back[pos] += 1
    return list(reversed(to_give_back))


def dijkstra(graph, start):
    # create a dictionary to store the shortest distances from start to others
    distances = {n: float("inf") for n in graph}
    distances[start] = 0  # distance is 0 b/ we start there
    # priority queue to explore nodes by the smallest known distance (greedy)
    pq = PriorityQueue()
    # Add the start node to the priority queue with distance 0
    pq.put((0, start))
    # Continue exploring nodes until the queue is empty
    while not pq.empty():
        # Get the node with the smallest distance ( minimum unvisited node)
        current_distance, current_node = pq.get()
        # skip processing this node if we have already found a shorter path to it
        if current_distance > distances[current_node]:
            continue
        # explore all neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the new tentative distance
            dist = current_distance + weight
            # if the newly combined distance is shorter update to the shortest neighbor
            if dist < distances[neighbor]:
                # update the shortest known distance for the neighbor node
                distances[neighbor] = dist
                # Add neighbor to priority queue for future exploration
                pq.put((dist, neighbor))
    return distances


def prim_mst(graph):
    # step 1: start from an arbitrary node
    start_node = next(iter(graph))
    # priority queue to select the smallest edge at each step
    pq = PriorityQueue()
    pq.put((0, start_node, start_node))
    # avoid cycles, we need to track visited nodes
    visited = set()
    # This will store the MST edges
    mst_edges = []
    # total cost of the MST (Sum of all edges weight in MST)
    total_weight = 0
    # continue until we have visited all nodes (this guarantees we have found the MST)
    while not pq.empty():
        # Step 2: Choose the edges with the smallest weight (greedy choice)
        weight, from_node, to_node = pq.get()
        # skip if we have already visited this node(avoid cycles)
        if to_node in visited:
            continue
        # step 3: Mark the node as visited
        visited.add(to_node)
        # if it's not the start node, add the edge to the MST
        if from_node != to_node:
            mst_edges.append((weight, from_node, to_node))
            total_weight += weight
        # Step 4: Explore the neighbors of the current node
        for neighbor, edge_weight in graph[to_node].items():
            if neighbor not in visited:
                pq.put((edge_weight, to_node, neighbor))
    return total_weight, mst_edges


if __name__ == "__main__":
    # ----------return_machine_change--------------#
    _denominations = [1, 2, 5, 10, 20, 50, 100]
    print(return_machine_change(30, _denominations))
    # returns [0, 0, 0, 1, 1, 0, 0]
    # 1x 10p, 1x 20p
    # -----------fractional_knapsack---------------#
    items = [
        Item(60, 10),  # Item with value 60 and weight 10
        Item(100, 20),  # Item with value 100 and weight 20
        Item(120, 30),  # Item with value 120 and weight 30
    ]
    max_value = fractional_knapsack(50, items)
    print(f"Maximum value that can be obtained: {max_value}")
    # -----------dijkstras------------------------#

    # Example usage: Creating a graph with nodes A, B, C, D, and E
    # This is similar to the graph diagram in the article
    graph = {
        'A': {'B': 4, 'C': 2},  # A is connected to B with a weight of 4 and to C with a weight of 2
        'B': {'A': 4, 'C': 1, 'D': 4},  # B is connected to A, C, and D
        'C': {'A': 2, 'B': 1, 'D': 3, 'E': 5},  # C is connected to A, B, D, and E
        'D': {'B': 4, 'C': 3, 'E': 1},  # D is connected to B, C, and E
        'E': {'C': 5, 'D': 1}  # E is connected to C and D
    }

    # We run Dijkstra's algorithm starting from node A (as described in the article)
    shortest_paths = dijkstra(graph, "A")

    # Output the shortest distances from start_node to all other nodes
    print("Shortest distances from node A")
    for node, distance in shortest_paths.items():
        # The result should show the shortest distance from A to every other node
        print(f"Distance to {node}: {distance}")

    # ------------------ prim_mst ------------------------#
    # Example graph (based on the article's example)
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }

    # Running Prim's algorithm on the graph to find the MST
    mst_weight, mst_edges = prim_mst(graph)

    # Output the MST and its total weight
    print(f"Minimum Spanning Tree weight: {mst_weight}")
    print("Edges in the MST:")
    for edge in mst_edges:
        print(f"{edge[0]} -- {edge[2]} -- {edge[1]}")
