import sys
def heapify(idx, size):
    largest = idx
    L = 2 * idx + 1
    R = 2 * idx + 2
    if L < size and arr[L] < arr[largest]:
        largest = L
    if R < size and arr[R] < arr[largest]:
        largest = R
    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest]
        heapify(largest, size)

def heap_sort():
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(0, i)

n = input()
arr=[]
for i in n:
    arr.append(i)
heap_sort()
for i in range(len(arr)):
    print(arr[i],end='')
