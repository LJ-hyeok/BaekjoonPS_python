import sys
n,m = map(int,sys.stdin.readline().split())
arr = list(0 for i in range(n+1))
vis = list(0 for i in range(n+1))

def dfs(cnt):
    if cnt==m:
        for i in range(0,m,1):
            print(arr[i],end=' ')
        print()
        return
    for i in range(1,n+1,1):
        if vis[i] == 0:
            vis[i] = 1
            arr[cnt] = i
            dfs(cnt+1)
            vis[i] = 0
dfs(0)