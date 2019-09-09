import sys; sys.stdin = open('weighted_graph.txt')

def BRUTEFORCE_SHORTEST(s):

    D = [0xfffff for _ in range(V + 1)]
    P = [0 for _ in range(V + 1)]
    D[s], P[s] = 0, s

    while True:
        stop = True
        for u in range(1, V + 1):       # 모든 정점에 대해
            for v, w in G[u]:           # 모든 간선에 대해
                if D[v] > D[u] + w:     # 간선 완화 수행
                    D[v] = D[u] + w
                    P[v] = u
                    stop = False

        if stop: break                  # D[] 값이 변경되지 않으면 중단

    print(D[1: V + 1])
    print(P[1: V + 1])

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

print(G)
BRUTEFORCE_SHORTEST(1)