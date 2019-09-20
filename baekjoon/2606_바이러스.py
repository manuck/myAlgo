import sys
sys.stdin = open('2606_input.txt')


def dfs(v):
    global ans
    if visited[v]:
        return
    visited[v] = 1

    for i in range(N):
        if g[v][i] == 1 and visited[i] == 0:
            ans += 1
            dfs(i)

N = int(input())
E = int(input())
# a = []
g = [[0 for _ in range(N)]for _ in range(N)]
visited = [0]*N
for i in range(E):
    # a.append(list(map(int, input().split())))
    a, b = map(int, input().split())
    g[a - 1][b - 1] = 1
    g[b - 1][a - 1] = 1

# for i in range(N):
#     print(g[i])

ans = 0
dfs(0)
print(ans)

