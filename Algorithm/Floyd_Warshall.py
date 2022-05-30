import sys
INF = 987654321

def floyd_warshall():
    for i in range(n):
        for j in range(n):
            if i==j:    continue
            for k in range(n):
                if i==k or j==k:    continue
                arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

def print_arr():
    for i in range(n):
        for j in range(n):
            if arr[i][j] != INF:
                print(arr[i][j],end=' ')
            else:
                print("0",end=' ')
        print()

#init
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = [[INF for col in range(n)] for row in range(n)]
for i in range(m):
    f,t,w = map(int,sys.stdin.readline().split())
    arr[f-1][t-1]= min(arr[f-1][t-1], w)
floyd_warshall()
print_arr()