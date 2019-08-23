import sys
sys.stdin = open('1260_input.txt')

def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    # print(visited)
    for w in range(1, N+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)


def bfs(x):
    global N, V, M, visited
    s = []
    visited = [0] * (N + 1)
    s.append(x)
    visited[x] = 1
    while len(s) != 0:
        # print(s)
        # print(visited)
        k = s.pop(0)
        print(k, end=" ")
        for w in range(1, N+1):
            if G[k][w] and visited[w] == 0:
                visited[w] = 1
                s.append(w)

N, M, V = map(int, input().split())
G = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    x, y = map(int, input().split())
    G[x][y] = 1
    G[y][x] = 1
# for i in range(N+1):
#     print(G[i])

dfs(V)
print()
bfs(V)