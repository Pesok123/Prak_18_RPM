def selection_sort(arr):
    """Сортировка выбором"""
    arr = arr.copy()
    swaps = 0
    comparisons = 0

    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1

    return arr, swaps, comparisons