def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]

    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]

    customList[i + 1], customList[high] = customList[high], customList[i + 1]
    return i + 1


def quick_sort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quick_sort(customList, low, pi - 1)
        quick_sort(customList, pi + 1, high)

# Example usage:
cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
quick_sort(cList, 0, len(cList) - 1)
print("Quick Sort:", cList)

