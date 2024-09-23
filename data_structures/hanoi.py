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


# Example usage:
n = 3  # Number of disks
tower_of_hanoi(n, 'A', 'C', 'B')  # A, B, C are the rods
