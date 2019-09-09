def DFS(v):
    S = []
    S.append(v)
    visit[v] = True
    print(v, end=" ")

    while len(S) > 0:
        for w in G[v]:
            if not visit[w]:
                S.append(v)
                v = w
                visit[w] = True
                print(v, end=" ")
                break
        else:
            v = S.pop()

# ----------------------------------------------
import sys
sys.stdin = open("DFS_input.txt", "r")

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
visit = [False for _ in range(V + 1)]

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

DFS(1)