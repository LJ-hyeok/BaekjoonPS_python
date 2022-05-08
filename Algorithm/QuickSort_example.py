def quicksort(A,first,last):
    p=A[first]
    left = first+1
    right = last

    while left <= right :
        while left <= last and A[left] < p :
            left+=1
        while A[right] > p :
            right-=1
        if left <= right :
            A[left],A[right] = A[right],A[left]
            left+=1
            right-=1
        A[first],A[right] = A[right],A[first]
        quicksort(A,first,right-1)
        quicksort(A,left,last)

A=[2,4,1,5,3,9]
print(A)
quicksort(A,0,len(A)-1)
print(A)
            





#quick sort algorithm
#in-place quick sort algorithm
