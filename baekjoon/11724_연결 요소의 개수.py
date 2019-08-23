import sys
sys.stdin = open('11724_input.txt')


def dfs(v):
    visited[v] = 1
    # print(v)
    for w in range(1, N+1):
        if g[v][w] == 1 and visited[w] == 0:
            dfs(w)


N, M = map(int, input().split())
g = [[0 for _ in range(N+1)]for _ in range(N+1)]
visited = [0] * (N+1)
res = 0
for i in range(M):
    x, y = map(int, input().split())
    g[x][y] = 1
    g[y][x] = 1

# for i in range(N):
#     print(g[i])

for i in range(1, len(visited)):
    if visited[i] == 0:
        res += 1
        dfs(i)

print(res)