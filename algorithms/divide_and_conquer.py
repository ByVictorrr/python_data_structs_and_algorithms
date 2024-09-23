
def merge_sort(arr: list[int]):
    # Base Case: If list has 0 or 1 element its sorted already
    if len(arr) <= 1:
        return
    # Divide: split the array into two halves
    midpoint = len(arr) // 2
    left_half = arr[:midpoint]  # Left half from start to midpoint
    right_half = arr[midpoint:]  # Right half from start to midpoint
    # Conquer: Recursively sort both halves (left and right side)
    merge_sort(left_half)
    merge_sort(right_half)
    # Merge: combine the two sorted halves
    i = j = k = 0  # initialize pointers for left_half, right_half, and main array
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]  # place the smaller element from left into the array
            i += 1  # move to the next element in left_hand
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    # If there are remaining elements in left_half
    # Happens if the left_half has more elements than right_half
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    # If there are remaining elements in right_half
    # Happens if the right_half has more elements than left_half
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def tower_of_hanoi(n, source, dest, spare):
    """
    Solves the Tower of Hanoi problem for n disks.

    Parameters:
    n (int): The number of disks.
    source (str): The name of the source rod.
    dest (str): The name of the destination rod.
    spare (str): The name of the spare rod.
    """
    # Base case: If only one disk, move it directly from source to dest.
    if n == 1:
        print(f"Move disk 1 from {source} to {dest}")
        return

    # Recursive case:
    # Step 1: Move n-1 disks from source to spare, using dest as the auxiliary.
    tower_of_hanoi(n - 1, source, spare, dest)

    # Step 2: Move the nth disk (the largest one) from source to dest.
    print(f"Move disk {n} from {source} to {dest}")

    # Step 3: Move the n-1 disks from spare to dest, using source as auxiliary.
    tower_of_hanoi(n - 1, spare, dest, source)




if __name__ == "__main__":
    arry = [23, 1, 32, 33, 31, 34, 4]
    merge_sort(arry)
    print(arry)
    # Example usage:
    n = 3  # Number of disks
    tower_of_hanoi(n, 'A', 'C', 'B')  # A, B, C are the rods