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

N=int(input())
A = list(map(int, input().split()))
#split() 공백을 기준으로 분리
#map(함수, 반복 가능한 자료형)
quicksort(A,0,N-1)
for i in range(1,N):
    A[i]+=A[i-1]
sum=0
for i in range(N):
    sum+=A[i]
print(sum)
