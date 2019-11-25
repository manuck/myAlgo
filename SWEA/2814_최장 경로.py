import sys
sys.stdin = open('2814_input.txt')

def dfs(len, v):
    global sol
    visited[v] = 1
    if sol < len:
        sol = len
    for w in range(1, n+1):
        if g[v][w] == 1 and visited[w] == 0:
            dfs(len + 1, w)
    visited[v] = 0
t = int(input())

for case in range(t):
    n, m = map(int, input().split())
    visited = [0] * (n+1)
    g = [[0 for _ in range(n+1)]for _ in range(n+1)]


    for i in range(m):
        x, y = map(int, input().split())
        g[x][y] = 1
        g[y][x] = 1

    sol = 0
    for i in range(n+1):
        dfs(1, i)

    print(f'#{case+1} {sol}')