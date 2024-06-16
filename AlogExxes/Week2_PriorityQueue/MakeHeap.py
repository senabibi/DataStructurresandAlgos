# python3


def heapify(data, n, i, swaps):
    """
    Ensure the subtree rooted at index i is a heap.
    Parameters:
    data: The list representing the heap.
    n: Total number of elements in the heap.
    i: Index of the current node.
    swaps: List to record the swaps made.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1     # left child
    right = 2 * i + 2     # right child

    # See if left child of root exists and is greater than root
    if left < n and data[i] < data[left]:
        largest = left

    # See if right child of root exists and is greater than the largest so far
    if right < n and data[largest] < data[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        data[i], data[largest] = data[largest], data[i]  # swap
        swaps.append((i, largest))
        # Heapify the root
        heapify(data, n, largest, swaps)

def build_heap(data):
    """
    Build a heap from `data` in-place and return the sequence of swaps.
    """
    swaps = []
    n = len(data)
    # Start from the first non-leaf node and move upwards
    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, swaps)
    return swaps

# Rest of the main function remains the same



def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

