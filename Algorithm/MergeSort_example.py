#import sys
#sys.setrecursionlimit(10**6)
A=[4,6,2,8,1,3,5,9,7]
def mergesort(A,first,last):
    if first >= last:
        return
    mergesort(A, first, (first+last)//2)
    mergesort(A, (first+last)//2+1, last)
    merge_two_sorted_list(A, first, last)
    
def merge_two_sorted_list(A,first,last):
    n = (first+last)//2
    i,j = first,n+1
    B=[]
    while i<=n and j<=last:
        if A[i]<=A[j]:
            B.append(A[i])
            j+=1
        else:
            B.append(A[j])
            j+=1
    for k in range(i,n+1):
        B.appned(A[k])
    for k in range(j,n+last+1):
        B.append(A[k])
    for i in range(first,last+1):
        A[i]=B[i-first]
        
print(A)
mergesort(A,0,len(A)-1)
print(A)
