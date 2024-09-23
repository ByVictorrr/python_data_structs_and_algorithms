import math

def print_tree(arr):
    """Prints the binary tree in a structured format based on array input."""
    n = len(arr)
    levels = math.ceil(math.log2(n + 1))  # Calculate the number of levels in the tree

    level_start = 0
    for level in range(levels):
        # Calculate the range for the current level
        level_end = min(level_start + 2 ** level, n)

        # Calculate space for node alignment
        space_before = " " * (2 ** (levels - level - 1))  # Space before the first node
        between_nodes = " " * (2 ** (levels - level) - 1)  # Space between nodes on the same level

        # Print the current level of nodes
        print(space_before + between_nodes.join(f"{arr[i]:2}" if i < n else "  " for i in range(level_start, level_end)))

        # Print the branches for the next level
        if 2 * level_start + 1 < n:
            branch_space_before = " " * (2 ** (levels - level - 2))  # Space before the first branch
            branch_between = " " * (2 ** (levels - level - 1))  # Space between branches
            print(branch_space_before, end="")
            for i in range(level_start, level_end):
                if 2 * i + 1 < n:  # Left child exists
                    print(" /", end="")
                else:
                    print("  ", end="")  # If no left child, print space

                print(branch_between, end="")  # Space between left and right branch

                if 2 * i + 2 < n:  # Right child exists
                    print("\\ ", end="")
                else:
                    print("  ", end="")  # If no right child, print space
            print()

        level_start = level_end


def max_heapify(arr, k):
    """Reorganize the heap such that it becomes Max-heap."""
    largest = k
    left_child = 2 * k + 1
    right_child = 2 * k + 2
    # if left_child exists and is larger than root
    if len(arr) > left_child and arr[left_child] > arr[largest]:
        largest = left_child
    # if right_child exists and is larger than current largest node
    if len(arr) > right_child and arr[right_child] > arr[largest]:
        largest = right_child
    # if root is not the largest, swap, and recursively max_heapify the rest of the tree
    if largest != k:
        arr[k], arr[largest] = arr[largest], arr[k]
        max_heapify(arr, largest)


def min_heapify(arr, k):
    """Reorganize the heap such that it becomes Min-heap."""
    smallest = k
    left_child = 2 * k + 1
    right_child = 2 * k + 2
    # if left_child exists and is less than root
    if len(arr) > left_child and arr[left_child] < arr[smallest]:
        smallest = left_child
    # if right_child exists and is less than current smallest node
    if len(arr) > right_child and arr[right_child] < arr[smallest]:
        smallest = right_child
    # if root is not the smallest, swap, and recursively min_heapify the rest of the tree
    if smallest != k:
        arr[k], arr[smallest] = arr[smallest], arr[k]
        min_heapify(arr, smallest)


if __name__ == "__main__":
    # Example usage
    print("----before max-heapify----")
    tree = [3, 9, 2, 1, 4, 5]
    print_tree(tree)
    max_heapify(tree, 0)
    print("----after max-heapify----")
    print_tree(tree)
    print("----before min-heapify----")
    tree = [3, 9, 2, 1, 4, 5]
    print_tree(tree)
    min_heapify(tree, 0)
    print("----after min-heapify----")
    print_tree(tree)
