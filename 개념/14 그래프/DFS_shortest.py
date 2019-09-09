import sys; sys.stdin = open('weighted_graph.txt')

def DFS_SHORTEST(u):
    for v, w in G[u]:
        if D[v] > D[u] + w:
            D[v] = D[u] + w
            P[v] = u
            DFS_SHORTEST(v)


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

D = [0xfffff for _ in range(V + 1)]
P = [0 for _ in range(V + 1)]
D[1], P[1] = 0, 1

DFS_SHORTEST(1)

print(D[1: V + 1])
print(P[1: V + 1])
