def merge_sort(customList):
    if len(customList) > 1:
        mid = len(customList) // 2
        left_half = customList[:mid]
        right_half = customList[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                customList[k] = left_half[i]
                i += 1
            else:
                customList[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            customList[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            customList[k] = right_half[j]
            j += 1
            k += 1

# Example usage:
cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
merge_sort(cList)
print("Merge Sort:", cList)

