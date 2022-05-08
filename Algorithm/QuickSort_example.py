import sys
sys.setrecursionlimit(10**6)
#RecursionError 발생 
#해결책: 파이썬이 제한하는 재귀함수의 깊이를 변경했음
A=list()
def quicksort(A,first,last):
    if first >= last:
        return
    p=first
    left = first+1
    right = last

    while left <= right :
        while left <= last and A[left] <= A[p] :
            left+=1
        while right > first and A[right] >= A[p] :
            right-=1

        if left>right:
            A[right],A[p] = A[p],A[right]
        else:
            A[left],A[right] = A[right],A[left]

    quicksort(A,first,right-1)
    quicksort(A,right+1,last)

A=[2,4,1,5,3,9]
print(A)
quicksort(A,0,len(A)-1)
print(A)
            


#b.c O(NlogN)
#w.c O(N^2)

#quick sort algorithm
#in-place quick sort algorithm
