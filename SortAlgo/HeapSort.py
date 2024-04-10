def heapify(customList, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and customList[left_child] > customList[largest]:
        largest = left_child

    if right_child < n and customList[right_child] > customList[largest]:
        largest = right_child

    if largest != i:
        customList[i], customList[largest] = customList[largest], customList[i]
        heapify(customList, n, largest)


def heap_sort(customList):
    n = len(customList)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(customList, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)

# Example usage:
cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
heap_sort(cList)
print("Heap Sort:", cList)

