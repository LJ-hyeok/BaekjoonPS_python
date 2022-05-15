def heapify(arr, idx, size):
    largest = idx
    L = 2 * idx + 1
    R = 2 * idx + 2
    if L < size and arr[L] > arr[largest]:
        largest = L
    if R < size and arr[R] > arr[largest]:
        largest = R
    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify(arr, largest, size)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

print(heap_sort([1,5,2,19,2,20]))