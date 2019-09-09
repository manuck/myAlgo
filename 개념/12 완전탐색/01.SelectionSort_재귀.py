

def findMaxIdx(arr, lo, hi):

    if lo == hi:
        return lo

    idx = findMaxIdx(arr, lo, hi - 1)
    idx = hi if arr[hi] < arr[idx] else idx

    return idx

def selectionSort(arr, lo, hi):

    if lo == hi:
        return

    idx = findMaxIdx(arr, lo, hi)

    arr[lo], arr[idx] = arr[idx], arr[lo]

    selectionSort(arr, lo + 1, hi)


# arr = [69, 10, 30, 2, 16, 8, 31, 22, 30]
arr = [1, 0, 1, 1, 1, 0, 0, 1, 0, 0]
selectionSort(arr, 0, len(arr) - 1)

print(arr)




